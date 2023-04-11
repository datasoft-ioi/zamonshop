

from rest_framework import serializers
from .models import Category, Subcategory, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['name', 'slug']


class SubcategorySerializer(serializers.ModelSerializer):
    children = ChildrenSerializer()
    # products = ProductSerializer(many=True)

    class Meta:
        model = Subcategory
        fields = ('id', 'name', 'slug', 'children', 'products')

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'subcategories')

