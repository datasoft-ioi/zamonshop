

from rest_framework import serializers
from .models import Category, Subcategory, Product




class ChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['name', 'slug']


class SubcategorySerializer(serializers.ModelSerializer):
    children = ChildrenSerializer()

    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'slug', 'children']

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'subcategories')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'