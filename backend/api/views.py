from rest_framework import generics
from django.shortcuts import get_object_or_404
from api.serializers import *
from store.models import Category, Product


class ListProductView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk:
            return get_object_or_404(Product,pk=pk)
        return Product.objects.all()
