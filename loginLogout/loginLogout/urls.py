"""loginLogout URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views as users_view
from main import views as main_view
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('login/',auth_view.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('', main_view.homePage, name='home'),
    path('admin/', admin.site.urls),
    path('signup/', users_view.register, name='signup')
]
