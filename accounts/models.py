from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.nickname