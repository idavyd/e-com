from django.urls import path, include
from api.views import *


urlpatterns = [
    path('products', ListProductView.as_view(), name='products'),
    path('products/<int:pk>', ListProductView.as_view(), name='getProductById')
]
