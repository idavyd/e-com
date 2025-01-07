from django.shortcuts import render
from rest_framework import generics
from api.serializers import GeneralSerializer
from django.contrib.auth.models import User


class ListUsersView(generics.ListAPIView):
    serializer_class = GeneralSerializer
    queryset = User.objects.all()

