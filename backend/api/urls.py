from django.contrib import admin
from django.urls import path, include
from api.views import ListUsersView


urlpatterns = [
    path('users/', ListUsersView.as_view(), name='users')
]
