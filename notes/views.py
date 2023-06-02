from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.contrib.auth.models import User

from .models import Post
from languages.forms import NotesForm

@login_required
def mynotes(request):
    blogs = Post.objects.filter(author=request.user).filter(status=Post.ACTIVE)
    return render(request, 'notes/blogpost.html', {
        'blogs': blogs
    })

@login_required
def note_contents(request, slug):
    notes = Post.objects.filter(status=Post.ACTIVE).get(slug=slug)
    return render(request, 'notes/contents.html', {
        'notes': notes,
    })

@login_required
def new_note(request):
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mynotes')
    else:
        form = NotesForm()

    return render(request, 'notes/notesform.html', {
        'form': form
    })

@login_required
def edit_blog(request, slug):
    note = Post.objects.get(slug)
    if request.method == 'POST':
        form = NotesForm(request.POST, request.FILES, instance=note)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your edits have been saved!')
            return redirect('mynotes')

    else:
        form = NotesForm(instance=note)
    return render(request, 'notes/notepost.html', {
        'note': note,
        'form': form,
        'title': 'Edit Notes'
    })

@login_required
def delete_blog(request, slug):
    blog = Post.objects.get(slug=slug)
    blog.status = blog.DELETED
    blog.save()
    messages.success(request, 'Your post has been successfully deleted')
    return redirect('mynotes')

