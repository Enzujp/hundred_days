from django.shortcuts import render, redirect, get_object_or_404

from .models import Blog

def blogposts(request):
    blogs = Blog.objects.filter(status=Blog.ACTIVE)
    return render(request, 'blog/blogpost.html', {
        'blogs': blogs
    })

def blog_contents(request, slug):
    # blogs = get_object_or_404(Blog, slug=slug, status=Blog.ACTIVE)
    blogs = Blog.objects.filter(status=Blog.ACTIVE).get(slug=slug)
    return render(request, 'blog/contents.html', {
        'blogs': blogs,
    })