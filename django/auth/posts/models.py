from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# ResizeToFill : 300 300 맞추고 넘치는 부분 잘라냄.
# ResizeToFit : 300 300 맟추고 남는 부분을 빈 공간으로 둠.
# google에 pilkit processors 검색

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # image = models.ImageField(blank=True)
    image = ProcessedImageField(
            upload_to = 'posts/images', #저장위치
            processors=[ResizeToFill(300,300)], #처리할 작업 목록
            format='JPEG',
            options={'quality':90}, #저장 포맷 관련 옵션
        )
    created_at = models.DateTimeField(auto_now_add=True) # create 될때 딱 한번 현재 시간
    updated_at = models.DateTimeField(auto_now=True) # 변경이 될 때 마다 현재 시각
    
    
    def __str__(self):
        return self.title
    

# Post : Comment = 1 : N
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    
    
    # on_delete 옵션
    #1. CASCADE : 부모가 삭제 되면, 자기 자신도 삭제.
    #2. PROTECT : 자식이 존재하면, 부모 삭제 불가능.
    #3. SET_NULL : 부모가 삭제되면, 자식의 부모 정보를 NULL로 변경.
    


#1. Create
#post = Post(ttle='Hello', content='World!')
# post.save()

#2. Read
#2.1. All
#posts = Post.object.all()
#2.2 Get one
#post = Post.objects.get(pk=1)
#2.3 filter(WHERE)
#posts = Post.objects.filter(title='Hello').all()
#post = Post.objects.filter(title='Hello').first()
#2.4 LIKE
#posts = Post.objects.filter(title__contains='He').all()
#2.5 order_by(정렬)
#posts = Post.objects.order_by('title').all() #오름차순
#posts = Post.objects.order_by('-title').all() #내림차순

#2.6 limit & offset
#[offset:offset+limit]
#posts = Post.objects.all()[1:2]

#3. Delete
#post = Post.objects.get(pk=2)
#post.delete()

#4. Update
#post = Post.objects.get(pk=1)
#post.title = 'Hi'
#post.save()