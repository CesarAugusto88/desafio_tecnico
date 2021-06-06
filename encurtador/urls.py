from django.urls import path, re_path
from . import views

app_name = 'encurtador'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    re_path(r'^(?P<uuid_curto>[\-\d\w]+)$',
                    views.GoToRedirectView.as_view()),

    path('my-links/',
                    views.MyLinksListView.as_view(), name='my_links'),
]
