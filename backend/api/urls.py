from django.urls import path, include
from api.views import *


urlpatterns = [
    path('products', ListProductView.as_view(), name='Products'),
    path('products/<int:pk>', ListProductView.as_view(), name='getProductById'),
    path('categories', ListCategoryView.as_view(), name='Categories'),
    path('products/<int:pk>', ListProductView.as_view(), name='getCategoryById'),

]






