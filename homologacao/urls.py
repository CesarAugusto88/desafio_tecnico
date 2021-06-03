from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'homologacao'

urlpatterns = [
    path("", views.Homologacao.as_view(), name='homologacao'),
]