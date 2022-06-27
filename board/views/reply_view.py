from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from ..models import Reply, Post
from ..serializers import ReplySerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class ReplyPagination(PageNumberPagination):
    page_size = 5

class ReplyListView(ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    pagination_class = ReplyPagination

class ReplyDetailView(APIView):
    def get(self, request, reply_id, format=None):
        reply = get_object_or_404(Reply, pk=reply_id)
        serializer = ReplySerializer(reply)
        return Response(serializer.data)

    def delete(self, request, reply_id, format=None):
        reply = get_object_or_404(Post, pk=reply_id)
        reply.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def replyCreate(request, post_id, format=None):
    post = Post.objects.get(pk=post_id)
    serializer = ReplySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user, post=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)