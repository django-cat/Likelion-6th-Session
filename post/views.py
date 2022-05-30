from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *

def index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts': posts})

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = PostForm()
        return render(request, 'post/create.html', {'form': form})

def update(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance = post)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = PostForm(instance = post)
        return render(request, 'post/update.html', {'form': form, 'id': id})

def delete(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect('index')