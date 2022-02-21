from django.contrib import admin
from django.contrib.admin.sites import site

#import Post

from .models import posts

# Register your models here.
admin.site.register(posts)