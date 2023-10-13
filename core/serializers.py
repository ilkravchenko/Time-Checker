from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'author', 'year', 'short_description']


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'author', 'year', 'short_description', 'long_description', 'date_of_last_reading']
