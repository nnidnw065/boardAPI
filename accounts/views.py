from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer, ProfileSerializer
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from rest_framework.generics import DestroyAPIView
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Profile

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

@api_view(['POST'])
def profile_create(request, format=None):
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors)

@api_view(['GET'])
def profile_view(request, user_id, format=None):
    user = get_object_or_404(User, pk=user_id)
    profile = Profile.objects.filter(user=user)
    if profile:
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)
    return Response({'message': '프로필이 없습니다.'})

@api_view(['PUT'])
def profile_update(request, profile_id, format=None):
    profile = get_object_or_404(Profile, pk=profile_id)
    serializer = ProfileSerializer(profile, data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)