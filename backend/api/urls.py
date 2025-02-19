from django.urls import path
from api.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('products', ListProductView.as_view(), name='Products'),
    path('products/<uuid:pk>', ListProductView.as_view(), name='getProductById'),
    path('categories', ListCategoryView.as_view(), name='Categories'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('categories/<uuid:pk>', ListCategoryView.as_view(), name='getCategoryById'),

]






