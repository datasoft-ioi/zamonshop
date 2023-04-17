from django.shortcuts import render

from .serializers import UserSerializer, CustomTokenObtainPairSerializer, UserRegisterSerializer

from .models import User

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework import routers, serializers, viewsets
from rest_framework_simplejwt.views import TokenObtainPairView





class UserSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

