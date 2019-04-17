from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField()

# User:Post = 1:N
class Post(models.Model):
    title = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# User:Comment = 1:N
# Post:Comment = 1:N
class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
# user1 = User.objects.create(name='Kim')
# user2 = User.objects.create(name='Lee')

# post1 = Post.objects.create(title='1글', user=user1) 
# post2 = Post.objects.create(title='2글', user=user2)
# post3 = Post.objects.create(title='3글', user=user2)


# c1 = Comment.objects.create(content='1글1댓글', user=user1, post=post1)
# c2 = Comment.objects.create(content='1글2댓글', user=user2, post=post1)
# c3 = Comment.objects.create(content='1글3댓글', user=user1, post=post1)
# c4 = Comment.objects.create(content='1글4댓글', user=user2, post=post1)
# c5 = Comment.objects.create(content='2글1댓글', user=user1, post=post2)
# c6 = Comment.objects.create(content='1글5댓글', user=user2, post=post1)
# c7 = Comment.objects.create(content='2글2댓글', user=user2, post=post2)