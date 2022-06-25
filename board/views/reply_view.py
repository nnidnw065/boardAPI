from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Reply
from ..serializers import ReplySerializer

@api_view(['GET'])
def reply_list(request):
    replys = Reply.objects.all()
    serializer = ReplySerializer(replys, many=True)
    return Response(serializer.data)