from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post


def list(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html', {'posts': posts})

# request: 외부의 요청이 담긴 정보
def create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')
    else:
        post_form = PostForm()
    post_form = PostForm()
    return render(request, 'posts/create.html', {'post_form': post_form})
    

#삭제
# variable routing => post_id
def delete(request, post_id):
    # pk로 해도 되고 id로 해도 되고
    # post = Post.objects.get(pk=post_id)
    # 지운걸 또 지우려 할 떄 존재하지 않는다고 알려줌
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    
    return redirect('posts:list')