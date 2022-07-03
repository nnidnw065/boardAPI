from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from rest_framework.generics import DestroyAPIView
from django.contrib.auth.models import User

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request, format=None):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    _, token = AuthToken.objects.create(user)
    return Response({
        'message': '회원가입을 마쳤습니다.',
        'token': token
    })

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request, format=None):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user)
    return Response({
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email
        },
        'token': token
    })

class UserDeleteAPI(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer