from .models import Book_DRF
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book_DRF
        fields = ['id', 'title', 'author', 'price']
