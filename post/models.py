from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
 
class Tag(models.Model):
    tag_name = models.CharField(max_length=256)
 
 
class Post(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    bump = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    '''tag = models.ManyToManyField(
        Tag, related_name = 'post', blank=True
    )'''


class PostImage(models.Model):
    parent = models.ForeignKey(
        Post, on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='post/image')


class Comment(models.Model):
    text = models.TextField()
    bump = models.IntegerField(default=0)
    time = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        Post, on_delete=models.CASCADE
    )


class CommentImage(models.Model):
    parent = models.ForeignKey(
        Post, on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='comment/image')