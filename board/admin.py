from django.contrib import admin
from .models import Post, Reply, Category

admin.site.register(Post)
admin.site.register(Reply)
admin.site.register(Category)