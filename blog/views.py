from django.shortcuts import render, redirect

from .models import Blog

def blogpost(request):
    blogs = Blog.objects.filter(status=Blog.ACTIVE)
    return render(request, 'blog/blogpost.html', {
        'blogs': blogs
    })