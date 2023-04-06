from django.shortcuts import render

from .models import Product, ProductCategory, Subcategory
from .serializers import ProductSerializer, ProductCategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import routers, serializers, viewsets, generics


from .serializers import CategorySerializer

# class CategoryList(generics.ListCreateAPIView):
#     queryset = Category.objects.all()


# class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()

from rest_framework import generics
from .models import Category, Subcategory
from .serializers import CategorySerializer

class CategoryList(APIView):
    # queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, *args, **kwargs):
        res = Category.objects.all()

        serializer = self.serializer_class(res, many=True)

        return Response(data=serializer.data)

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class ProductSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCategorySet(viewsets.ModelViewSet):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()

class CategorySet(APIView):
    serializer_class = ProductCategorySerializer
    # response = ProductCategory.objects.all()

    def get(self, *args, **kwargs):
        res = ProductCategory.objects.all()
        print(res)
        serializer = self.serializer_class(res, many=True)
        print(serializer.data)
        return Response(data=serializer.data)
    



def index(request):
    pass

