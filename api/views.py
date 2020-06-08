from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import viewsets

from product.models import *

from api.serializers import *


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('created')
    serializer_class = ProductSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('category_name')
    serializer_class = CategorySerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all().order_by('brand_name')
    serializer_class = BrandSerializer
