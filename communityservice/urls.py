from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Redirects for the default allauth pages
    path('accounts/login/', lambda request: redirect('/')),
    path('accounts/signup/', lambda request: redirect('/')),
]