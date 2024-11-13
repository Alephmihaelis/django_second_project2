
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.utils import timezone

def home(request):
    posts = Post.objects.filter(status='ativo', expiration__gte=timezone.now()).order_by('-date')
    return render(request, 'posts/home.html', {'posts': posts})

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    
    return render(request, 'posts/new_post.html', {'form': form})
