from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import CreateView, ListView, TemplateView

from .forms import LoginForm


class Homologacao(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('homologacao:homologacao')
    template_name = 'homologacao.html'


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                   password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated',
                        successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    return render(request, 'sua-app/login.html', {'form': form})