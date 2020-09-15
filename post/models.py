from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']


class Gallery(models.Model):
    title = models.CharField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


class Photo(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    photo_url = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
