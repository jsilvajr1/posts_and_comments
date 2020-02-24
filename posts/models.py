from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=255)
   

class Comment(models.Model):
    body = models.CharField(max_length=255)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)