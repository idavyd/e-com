from django.urls import path, include
from api.views import *


urlpatterns = [
    path('users/', ListUsersView.as_view(), name='users'),
    path('products_list/', ListProductView.as_view(), name='products'),
    path('categories_list/', ListCategoryView.as_view(), name='categories')
]
