from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Post
from ..serializers import PostSerializer

@api_view(['GET'])
def index(request):
    return Response('Hello Board')

@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

