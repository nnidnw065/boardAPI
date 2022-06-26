from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from ..models import Reply, Post
from ..serializers import ReplySerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

class ReplyPagination(PageNumberPagination):
    page_size = 5

class ReplyListViewSet(ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    pagination_class = ReplyPagination

# @api_view(['GET'])
# def replyList(request, format=None):
#     replys = Reply.objects.all()
#     serializer = ReplySerializer(replys, many=True)
#     return Response(serializer.data)

@api_view(['POST'])
def replyCreate(request, post_id, format=None):
    post = Post.objects.get(pk=post_id)
    serializer = ReplySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user, post=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def replyDetail(request, reply_id, format=None):
    try:
        reply = Reply.objects.get(pk=reply_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReplySerializer(reply)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        reply.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)