from django.urls import path, include
from api.views import *


urlpatterns = [
    path('products_list/', ListProductView.as_view(), name='products'),
    path('categories_list/', ListCategoryView.as_view(), name='categories'),
    path('image_add/', AddProductImageView.as_view(), name='image_add')
]
