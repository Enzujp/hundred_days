from django.shortcuts import render, redirect, get_object_or_404
from languages.models import Notepad
from languages.forms import NotepadForm
# Create your views here.

def detail(request, slug):
    notes = Notepad.objects.filter(status=Notepad.ACTIVE).filter(slug=slug)
    return render(request, 'notepad/my_notes.html', {
        'notes': notes
    })
    

def my_notes(request):
    notes = request.user.notepads.exclude(status=Notepad.DELETED)
    return render(request, 'notepad/my_notes.html', {
        'notes': notes
    })
    

def new_notes(request):
    if request.method == 'POST':
        form = NotepadForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
        
            return redirect ('my-notes')
    else:
        form = NotepadForm()
        
    return render(request, 'notepad/new_notes.html', {
        'form': form
    })


def edit_note(request, slug):
    note = Notepad.objects.filter(user=request.user).filter(status=Notepad.ACTIVE).get(slug=slug)
    if request.method == 'POST':
        form = NotepadForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            return redirect('my-notes')
    else:
        form = NotepadForm(instance=note)

    return render(request, 'notepad/detail.html', {
        'note': note,
        'form': form
    })


def delete_notes(request, slug):
    note = Notepad.objects.filter(user=request.user).filter(status=Notepad.ACTIVE).get(slug=slug)
    note.status = note.DELETED
    note.save()
    return redirect('my-notes')