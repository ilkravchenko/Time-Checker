from rest_framework import serializers
from reading.models import ReadingSession
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'author', 'year', 'short_description']


class ReadingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingSession
        fields = ['id', 'user', 'started_at', 'ended_at', 'read_time', 'book']


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'author', 'year', 'short_description', 'long_description', 'date_of_last_reading']
