from django.shortcuts import render, redirect
from .models import Post, Comment
# Create your views here.
def new(request):
    return render(request, 'new.html')
    
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    post = Post(title=title, content=content)
    post.save()
    
    return redirect(f'posts:detail', post.pk)
    
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})
    
def detail(request,post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'detail.html', {'post':post})
    
def delete(request,post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return  redirect('posts:list')
    

def edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'edit.html', {'post':post})
    
def update(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.title = request.POST.get('title')
    post.content = request.POST.get('content')
    post.save()
    
    return redirect(f'/posts/{post_id}/')
    
def comments_create(request, post_id):
    post = Post.objects.get(pk=post_id)
    
    content = request.POST.get('content')
    
    comment = Comment(post=post, content=content)
    comment.save()
    
    return redirect('posts:detail', post.pk)