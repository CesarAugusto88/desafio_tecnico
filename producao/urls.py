from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'producao'

urlpatterns = [
    path("", views.Link.as_view(), name='producao'),
]