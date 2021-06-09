from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views import View
from django.http import HttpResponseNotFound, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.urls import reverse_lazy

from perfil.models import Perfil
from perfil.forms import UserForm, PerfilForm

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# from perfil.utils import render_to_pdf

from django.contrib.auth.mixins import LoginRequiredMixin


class ProgressaoAcesso(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('perfil:criar')
    model = Perfil
    fields = ['usuario', 'acessos']
    template_name = 'perfil/acessos.html'
    success_url = reverse_lazy('acessos')  # listar-progressao

    def form_valid(self, form):

        # Antes do super não foi criado o objeto nem salvo no banco
        form.instance.usuario = self.request.user

        url = super().form_valid(form)

        self.object.save()

        return url


# Gera relatorio pdf
class GenerateRelatorioPdfAcessos(View):
    """Gerar pdf de 'relatorio.html' de acessos."""
    def get(self, request, *args, **kwargs):
        context = {}
        usuario = request.user
        try:
            user_acessos = Perfil.objects.get(usuario=usuario)

        except Exception:
            return HttpResponseNotFound(
                            'Erro: <h1>Você é um Administrador</h1>')
        if user_acessos:
            context = {
                'acessos': user_acessos.acessos
            }
            # pdf = render_to_pdf('relatorio.html', context)

        else:
            return HttpResponseNotFound('<h1>Page not found</h1>')
        # return HttpResponse(pdf, content_type='perfil/pdf')
        return render(request, "perfil/relatorio.html", context)


# Projeto encurtador de links com django
class LoginRequiredMixin(object):
    """
        Você pode conferir a explicação da criação desse Mixin em um post meu:
        http://douglasmiranda.com/artigo/login-required-mixin-django-class-based-generic-views-iv/
    """
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class BasePerfil(View):
    template_name = 'perfil/criar.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.perfil = None

        if self.request.user.is_authenticated:
            self.perfil = Perfil.objects.filter(
                usuario=self.request.user
            ).first()

            self.contexto = {
                'userform': UserForm(
                    data=self.request.POST or None,
                    usuario=self.request.user,
                    instance=self.request.user,
                ),
                'perfilform': PerfilForm(
                    data=self.request.POST or None,
                    instance=self.perfil
                )
            }
        else:
            self.contexto = {
                'userform': UserForm(
                    data=self.request.POST or None
                ),
                'perfilform': PerfilForm(
                    data=self.request.POST or None
                )
            }

        self.userform = self.contexto['userform']
        self.perfilform = self.contexto['perfilform']

        if self.request.user.is_authenticated:
            self.template_name = 'perfil/atualizar.html'

        self.renderizar = render(
            self.request, self.template_name, self.contexto)

    def get(self, *args, **kwargs):
        return self.renderizar


class Criar(BasePerfil):
    def post(self, *args, **kwargs):
        if not self.userform.is_valid() or not self.perfilform.is_valid():
            messages.error(
                self.request,
                'Existem erros no formulário de cadastro. Verifique se todos '
                'os campos foram preenchidos corretamente.'
            )

            return self.renderizar

        username = self.userform.cleaned_data.get('username')
        password = self.userform.cleaned_data.get('password')
        email = self.userform.cleaned_data.get('email')
        first_name = self.userform.cleaned_data.get('first_name')
        last_name = self.userform.cleaned_data.get('last_name')

        # Usuário logado - alterações
        if self.request.user.is_authenticated:
            usuario = get_object_or_404(
                User, username=self.request.user.username)

            usuario.username = username

            if password:
                usuario.set_password(password)

            usuario.email = email
            usuario.first_name = first_name
            usuario.last_name = last_name
            usuario.save()

            if not self.perfil:
                self.perfilform.cleaned_data['usuario'] = usuario
                print(self.perfilform.cleaned_data)
                perfil = Perfil(**self.perfilform.cleaned_data)
                perfil.save()
            else:
                perfil = self.perfilform.save(commit=False)
                perfil.usuario = usuario
                perfil.acessos += 1
                perfil.save()

        # Usário não logado (novo)
        else:
            usuario = self.userform.save(commit=False)
            usuario.set_password(password)
            usuario.save()

            perfil = self.perfilform.save(commit=False)
            perfil.usuario = usuario
            perfil.save()

        if password:
            autentica = authenticate(
                self.request,
                username=usuario,
                password=password
            )

            if autentica:
                login(self.request, user=usuario)

        self.request.session.save()

        messages.success(
            self.request,
            'Seu cadastro foi criado ou atualizado com sucesso.'
        )

        messages.success(
            self.request,
            'Você fez login.'
        )

        return redirect('/')


class Atualizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Atualizar')


class Login(View):
    def post(self, request, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        try:
            if not username or not password:
                messages.error(
                    self.request,
                    'Usuário ou senha inválidos.'
                )
                return redirect('perfil:criar')

            usuario = authenticate(
                self.request, username=username, password=password)
            if usuario:
                # Contador acessos de login do user
                user_acessos = Perfil.objects.get(usuario=usuario)
                user_acessos.acessos += 1
                user_acessos.save()

            if not usuario:
                messages.error(
                    self.request,
                    'Usuário ou senha inválidos.'
                )
                return redirect('perfil:criar')

        except Exception:
            return HttpResponseNotFound(
                            '''Erro: <h1>Você é um Administrador</h1>
                               Entre com um usuário comum.''')
        login(self.request, user=usuario)

        messages.success(
            self.request,
            'Você está logado no sistema.'
        )

        return redirect('/')


class Logout(View):
    def get(self, *args, **kwargs):

        logout(self.request)

        self.request.session.save()

        return redirect('/')