from django.shortcuts import render

from .models import Product, ProductCategory
from .serializers import ProductSerializer, ProductCategorySerializer
from rest_framework.views import APIView

from rest_framework import routers, serializers, viewsets, generics


class ProductSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCategorySet(viewsets.ModelViewSet):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()

class CategorySet(APIView):
    serializer_class = ProductCategorySerializer
    response = ProductCategory.objects.all()


def index(request):
    pass

