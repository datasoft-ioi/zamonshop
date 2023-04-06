from rest_framework import routers, serializers, viewsets

from .models import Product, ProductCategory, Subcategory

from rest_framework import serializers
from .models import Category, Subcategory

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'subcategories']
        


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product    
        fields = '__all__'


class ProductCategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = ProductCategory
        fields = ['name', 'description', 'subcategories']
        # depth = 1

