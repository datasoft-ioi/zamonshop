from django.shortcuts import render

from .serializers import UserSerializer, MyTokenObtainPairSerializer

from .models import User

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework import routers, serializers, viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .serializers import MyTokenObtainPairSerializer, RegisterSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/users/token/',
        '/users/register/',
        '/users/token/refresh/'
    ]
    return Response(routes)



# class UserSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserCreate(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserRegisterSerializer


# class UserRegistrationView(generics.CreateAPIView):
#     serializer_class = UserRegisterSerializer
#     permission_classes = (AllowAny,)


# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer

