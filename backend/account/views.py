from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.cache import cache
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObatainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        print(user.username)
        return token


class MyTokenObtainPair(TokenObtainPairView):
    serializer_class = MyTokenObatainPairSerializer


class UserAuthenticationView(APIView):

    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'errors': 'The requested user does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        login(request, user)
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRegistrationView(APIView):

    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password1')
        email = request.data.get('email')
        user_name = User.objects.filter(username=username)
        print("username", user_name)
        if user_name:
            result = 'Username already taken'
        elif request.data['password1'] != request.data['password2']:
            result = "Passwords don't match"
        else:
            User.objects.create_user(
                username=username, email=email, password=password)
            result = "User created successfully"

        return Response({'response': result})
