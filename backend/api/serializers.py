from rest_framework import serializers
from django.contrib.auth.models import User
from store.models import Product, Category


class GeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'category', 'short_description', 'price', 'images', 'stock', 'in_stock')
