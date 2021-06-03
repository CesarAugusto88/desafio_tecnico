from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'dev'

urlpatterns = [
    path("", views.Usuario.as_view(), name='usuario'),
]