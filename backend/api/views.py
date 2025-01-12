from django.shortcuts import render
from rest_framework import generics
from api.serializers import GeneralSerializer
from django.contrib.auth.models import User
from store.models import Category, Product


class ListUsersView(generics.ListAPIView):
    serializer_class = GeneralSerializer
    queryset = User.objects.all()


class ListProductView(generics.ListAPIView):
    serializer_class = GeneralSerializer
    queryset = Product.objects.all()


class ListCategoryView(generics.ListAPIView):
    serializer_class = GeneralSerializer
    queryset = Category.objects.all()

