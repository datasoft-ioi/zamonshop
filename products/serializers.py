from rest_framework import routers, serializers, viewsets

from .models import Product, ProductCategory


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product    
        fields = '__all__'


class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory    
        fields = "__all__"
        depth = 1

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory    
        fields = "__all__"
        depth = 1
