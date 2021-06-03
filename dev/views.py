from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from django.views.generic import CreateView, ListView, TemplateView

#from dev.models import Cliente, Funcionario

#from dev.forms import FuncionarioForm, ClienteForm


class Usuario(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('dev:usuario')
    template_name = 'usuario.html'