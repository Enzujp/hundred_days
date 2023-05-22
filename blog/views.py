from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .models import Blog
from languages.forms import BlogForm

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


def new_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('blogs')
    else:
        form = BlogForm()

    return render(request, 'blog/blogform.html', {
        'form': form
    })


def edit_blog(request, id):
    blog = Blog.objects.filter.get(id=id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your edits have been saved!')
            return redirect('blogs')

    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/blogpost.html', {
        'blog': blog,
        'form': form,
        'title': 'Edit Blog'
    })

def delete_blog(request, id):
    blog = Blog.objects.get(id=id)
    blog.status = blog.DELETED
    blog.save()
    messages.success(request, 'Your post has been successfully deleted')
    return redirect('blogs')