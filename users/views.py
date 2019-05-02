from django.shortcuts import render

from . import models

from . import serializers

from rest_framework import generics


class UserListView(generics.ListCreateAPIView):

	queryset = models.CustomUser.objects.all()

	serializer_class = serializers.UserSerializer