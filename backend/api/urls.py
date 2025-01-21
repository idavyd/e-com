from django.urls import path, include
from api.views import *


urlpatterns = [
    path('products/', ListProductView.as_view(), name='products')
]
