from django.shortcuts import render
from .models import MenuItem
from .serializers import MenuItemSerializers
from rest_framework import generics

# Create your views here.

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializers

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializers
