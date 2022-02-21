from django.urls import path
from appTwo import views

urlpatterns = [
    path('', views.my_users, name='users'),
]
