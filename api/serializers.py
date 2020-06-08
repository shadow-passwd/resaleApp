from rest_framework import serializers

from django.contrib.auth.models import User

from product.models import *


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Product
#         fields="__all__"

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    category = serializers.ReadOnlyField(source='category.category_name')
    brand = serializers.ReadOnlyField(source='brand.brand_name')

    class Meta:
        model = Product
        fields = '__all__'
        # fields = ['product_name', 'description', 'user']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"
