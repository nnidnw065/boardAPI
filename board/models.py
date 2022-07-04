from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=20)
    

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='post_author')
    title = models.CharField(max_length=64)
    content = models.TextField()
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='post_like', blank=True)
    view_count = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Reply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reply_author')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='reply_like', blank=True)

    def __str__(self):
        return self.content

class PostCount(models.Model):
    ip = models.CharField(max_length=30)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.ip