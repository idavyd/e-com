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
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'short_description', 'price', 'stock', 'images')

    def get_images(self, obj):
        # Check if the product has images
        if obj.images.exists():
            return ProductImageSerializer(obj.images.all(), many=True, context=self.context).data
        else:
            # Return a default image message or URL if no images are present
            return [{
                "image_url": self.context.get('request').build_absolute_uri('/static/product-default-image.jpg')
            }]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['id'] = str(instance.pk)
        return representation

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name')