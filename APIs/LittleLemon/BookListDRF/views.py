from django.shortcuts import render
from .models import Book_DRF
from .serializers import BookSerializer
from rest_framework import generics


# Create your views here.

class BookView(generics.ListCreateAPIView):
    queryset = Book_DRF.objects.all()
    serializer_class = BookSerializer


class SingleBookView(generics.RetrieveUpdateAPIView):
    queryset = Book_DRF.objects.all()
    serializer_class = BookSerializer
