from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Post, PostCount, Category
from ..serializers import PostSerializer
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class PostPagination(PageNumberPagination):
    page_size = 8

class PostListView(ModelViewSet):
    serializer_class = PostSerializer
    pagination_class = PostPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        category = self.kwargs['category_name']
        post_list = Post.objects.filter(category__name=category).order_by('-created_at')
        return post_list

class PostDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, post_id, format=None):
        post = get_object_or_404(Post, pk=post_id)
        ip = get_client_ip(request)
        postcnt = PostCount.objects.filter(ip=ip, post=post).count()

        if postcnt == 0:
            pc = PostCount(ip=ip, post=post)
            pc.save()
            if post.view_count:
                post.view_count += 1
            else:
                post.view_count = 1
            post.save()

        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, post_id, format=None):
        post = get_object_or_404(Post, pk=post_id)
        serializer = PostSerializer(post, data=request.data)
        if request.user.is_authenticated:
            if serializer.is_valid():
                serializer.author = request.user
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        return Response({'message': '????????? ??? ???????????????.'})

    def delete(self, request, post_id, format=None):
        post = get_object_or_404(Post, pk=post_id)
        if request.user.is_authenticated:
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'message': '????????? ??? ???????????????.'})

@api_view(['POST'])
def postCreate(request, format=None):
    serializer = PostSerializer(data=request.data)
    if request.user.is_authenticated:
        if serializer.is_valid():
            serializer.save(author=request.user) # ???????????? ?????? ????????? ?????? ????????? ????????????
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors)

@api_view(['POST'])
def postLike(request, pk, format=None):
    post = get_object_or_404(Post, pk=pk)
    serializer = PostSerializer(post)
    user = request.user
    if user in post.like.all():
        post.like.remove(user)
    else:
        post.like.add(user)
    return Response(serializer.data)