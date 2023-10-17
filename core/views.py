from django.http import JsonResponse
from .models import Book
from reading.models import ReadingSession
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer, BookDetailSerializer, ReadingSessionSerializer
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET', 'POST'])
def book_list(request, format=None):
    """
    get all books, serialize them and return JSON
    """
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(data={"Books": serializer.data}, safe=True)

    if request.method == 'POST':
        serializer = BookDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def reading_list(request, format=None):
    """
    get all readers, serialize them and return JSON
    """
    if request.method == 'GET':
        # Check for query parameters and filter the results accordingly
        user = request.query_params.get('user')
        book = request.query_params.get('book')

        readers = ReadingSession.objects.all()

        if user:
            readers = readers.filter(user=user)

        if book:
            readers = readers.filter(book=book)

        serializer = ReadingSessionSerializer(readers, many=True)
        return JsonResponse(data={"Readers": serializer.data}, safe=True)

    if request.method == 'POST':
        serializer = ReadingSessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, id, format=None):
    """
    get book by id, serialize it and return JSON
    """
    try:
        book = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BookDetailSerializer(book)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        serializer = BookDetailSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def reading_details(request, id, format=None):
    """
    get reader by id of data, serialize it and return JSON
    """
    try:
        reader_id = ReadingSession.objects.get(pk=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ReadingSessionSerializer(reader_id)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        serializer = ReadingSessionSerializer(reader_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        reader_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
