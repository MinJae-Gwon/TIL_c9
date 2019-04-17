from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.TextField()
    


# 정리
# class Post : Django - Model, DB - Table
# post = Post() : Django - Instance or Object, DB - Record or Row
# title : Django - Field, DB - Column

# CRUD
# 1. Create
# 방법(1). 
# post1 = Post(title='hello-1')
# post1.save()

# 방법(2).=> object라는 매니저가 save까지 알아서 해줌, 따로 save 불필요
# post2 = Post.objects.create(title='hello-2')

# 방법(3).
# post3.title = 'hello-3'
# post3.save()
# post3.title = 'hello-4'
# post3.save() => update됨

# 2. Read
# (1) all
# posts = Post.objects.all() => QuerySet이란 dataset, 복수형 변수에 저장 필요

# (2)-1
# post - Post.objects.get(pk=1) # id=1 가능, title='hello-1'도 가능

# (2)-2 (views.py 한정)
# from django.shortcuts import get_objects_or_404
# post = get_object_or_404(Post, pk=1) # id=1 가능, title='hello-1'도 가능

# (2)-3
# post =  Post.objects.filter(pk=1)[0] # id=1 가능, title='hello-1'도 가능
# post =  Post.objects.filter(pk=1).first() # id=1 가능, title='hello-1'도 가능(같은 값이 여러개일 때 맨 처음만 나옴)

# (2)-4. Where(filter)
# posts = Post.objects.filter(title='hello-1')
# post = Post.objects.filter(title='hello-1').first() # 또는 [0]

# LIKE
# posts = Post.objects.filter(title__contains='lo')

# order_by
# posts = Post.objects.order_by('title') # 제목 오름차순
# posts = Post.objects.order_by('-title') # 제목 내림차순

# offset & limit
# Post.objects.all()[0] #=> offset 0 limit 1
# Post.object.all()[1] #=> offset 1 limit 1
# Post.object.all()[1:3] #=> offset 1 limit 2
# Post.object.all()[offset:offset+limit]

# 3. Update
# post = Post.objects.get(pk=1)
# post.title = 'hello-5'
# post.save() # 실제 database에 저장

# 4. delete
# post = Post.objects.get(pk=1)
# post.delete()
# (1, {'crud.Post': 1}) # 삭제 됐다는 message

# 한줄로
# Post.objects.get(pk=1).delete()