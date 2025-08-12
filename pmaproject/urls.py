from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from communityservice import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('communityservice.urls')),
    path('accounts/', include('allauth.urls')),  # Ensure allauth URLs are included

    # Redirects for the default allauth pages
    path('accounts/login/', lambda request: redirect('/')),
    path('accounts/signup/', lambda request: redirect('/')),
]