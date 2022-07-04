from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from ..serializers import PostSerializer
from django.shortcuts import get_object_or_404
from ..models import Post

class PostPagination(PageNumberPagination):
    page_size = 8

class IndexViewSet(ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    pagination_class = PostPagination
    permission_classes = [AllowAny]