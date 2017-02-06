
from django.conf.urls import url
from src.accounts.views import (
    logout_view,
    settings, password,
    register_view
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^register/', register_view, name='register'),
    url(r'^settings/$', settings, name='settings'),
    url(r'^settings/password/$', password, name='password'),
]
