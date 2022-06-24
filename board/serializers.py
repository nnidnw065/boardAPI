from rest_framework import serializers
from .models import Post, Reply

class PostSerializer(serializers.ModelSerializer):
    model = Post
    fields = [
        'author',
        'title',
        'content',
        'created_at',
        'updated_at',
    ]

class ReplySerializer(serializers.ModelSerializer):
    model = Reply
    fields = [
        'author',
        'content',
        'created_at',
    ]