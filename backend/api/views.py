from rest_framework import generics
from rest_framework.exceptions import NotFound, ValidationError
from api.serializers import *
from store.models import Category, Product


class ListProductView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if pk:
            try:
                pk = int(pk)
            except ValueError:
                raise ValidationError('Invalid id format')
            queryset = Product.objects.filter(pk=pk)
            if not queryset.exists():
                raise NotFound("Product not found.")
            return queryset
        return Product.objects.all()


class ListCategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if pk:
            try:
                pk = int(pk)
            except ValueError:
                raise ValidationError('Invalid id format')
            queryset = Category.objects.filter(pk=pk)
            if not queryset.exists():
                raise NotFound("Product not found.")
            return queryset
        return Category.objects.all()
