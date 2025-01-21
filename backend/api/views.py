from rest_framework import generics
from api.serializers import *
from store.models import Category, Product


class ListProductView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

