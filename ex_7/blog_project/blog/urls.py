from django.urls import path
from django.contrib.auth import views as auth_view
from blog.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('posts/', PostListView.as_view(), name='blog-home'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='blog-detail'),
    path('posts/new/', PostCreateView.as_view(), name='blog-new'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='blog-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='blog-delete'),

]
