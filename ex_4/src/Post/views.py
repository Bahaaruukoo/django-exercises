from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .models import posts

def posts_list_view(request):
    posts_object = posts.objects.all()
    context = {
        'posts_object':posts_object
    }
    return render(request, "posts/post.html", context)