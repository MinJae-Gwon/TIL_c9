from django.db import models

# Create your models here.
class Bull(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()