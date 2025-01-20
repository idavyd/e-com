from rest_framework import serializers
from store.models import *


class ProductImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ['image_url']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)  # Build full URL
        return request.build_absolute_uri('/static/images/default_product.jpg')


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'short_description', 'price', 'stock', 'images')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name')