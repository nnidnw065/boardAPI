from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from ..models import Reply, Post
from ..serializers import ReplySerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny

class ReplyPagination(PageNumberPagination):
    page_size = 5

class ReplyListView(ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    pagination_class = ReplyPagination
    permission_classes = [AllowAny]

class ReplyDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, reply_id, format=None):
        reply = get_object_or_404(Reply, pk=reply_id)
        serializer = ReplySerializer(reply)
        return Response(serializer.data)

    def delete(self, request, reply_id, format=None):
        reply = get_object_or_404(Post, pk=reply_id)
        if request.user.is_authenticated:
            reply.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'message': '로그인 후 가능합니다.'})

@api_view(['POST'])
def replyCreate(request, post_id, format=None):
    post = Post.objects.get(pk=post_id)
    serializer = ReplySerializer(data=request.data)
    if request.user.is_authenticated:
        if serializer.is_valid():
            serializer.save(author=request.user, post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({'message': '로그인 후 가능합니다.'})

@api_view(['POST'])
def reply_like(request, pk, format=None):
    reply = get_object_or_404(Reply, pk=pk)
    serializer = ReplySerializer(reply)
    user = request.user
    if user in reply.like.all():
        reply.like.remove(user)
    else:
        reply.like.add(user)
    return Response(serializer.data)