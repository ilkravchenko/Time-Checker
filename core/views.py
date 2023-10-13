from django.http import JsonResponse
from .models import Book
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer, BookDetailSerializer
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
        return JsonResponse({"Books": serializer.data}, safe=True)

    if request.method == 'POST':
        serializer = BookDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, id, format=None):
    """
    get book by id, serialize it and return JSON
    """
    try:
        drink = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BookDetailSerializer(drink)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = BookDetailSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
