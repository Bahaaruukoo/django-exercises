"""django_project URL Configuration


"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog import views as blog_view
from users import views as users_view
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', blog_view.about, name='blog-about'),
    path('register/', users_view.user_register, name='register'),
    path('profile/', users_view.profile, name='profile'),
    path('login/', auth_view.LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done', auth_view.PasswordResetDoneView.as_view(template_name='users/password_reset_Done.html'), name='password_reset_done'),
    path('password-reset-complete', auth_view.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('password-reset-confirm/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
