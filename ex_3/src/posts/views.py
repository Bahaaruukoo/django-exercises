from django.shortcuts import render

# Create your views here.
from .models import Post

def post_list_view(request):
    post_object = Post.objects.all()
    context = {
        'post_object': post_object
    }
    return render(request, "posts/index.html", context)