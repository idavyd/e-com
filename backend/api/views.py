from django.shortcuts import render
from rest_framework import generics
from api.serializers import *
from django.contrib.auth.models import User
from store.models import Category, Product


class ListProductView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ListCategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class AddProductImageView(generics.CreateAPIView):
    serializer_class = ProductImageSerializer
    queryset = ProductImage.objects.all()

