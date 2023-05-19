from django.shortcuts import render, redirect, get_object_or_404

from .models import Blog

def blogposts(request):
    blogs = Blog.objects.filter(status=Blog.ACTIVE)
    return render(request, 'blog/blogpost.html', {
        'blogs': blogs
    })

def blog_contents(request, id):
    blogs = Blog.objects.filter(status=Blog.ACTIVE).get(id=id)
    return render(request, 'blog/contents.html', {
        'blogs': blogs,
    })

# def new_blog(request):
#     if request.method == "POST":
#         form = BlogForm(request.POST)

