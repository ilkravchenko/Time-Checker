from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book
import json
import pytest
from .serializers import BookSerializer, BookDetailSerializer

client = APIClient()


@pytest.mark.django_db
def create_test_book():
    return Book.objects.create(
        name='Test Book',
        author='Test Author',
        year=2022,
        short_description='A test book for testing.',
    )


@pytest.mark.django_db
def test_book_list_view_GET():
    # Create a test book
    book = create_test_book()

    # Get the list of books
    response = client.get(reverse('all_books'))

    # Assert that the response status code is 200 OK
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_book_list_view_POST():
    # Send a POST request to create a new book
    url = reverse('all_books')

    new_data = {
        'name': 'Updated Book Name',
        'author': 'Updated Author',
        'year': 2023,
        'short_description': 'Updated description',
        'long_description': 'Updated long description',
        'date_of_last_reading': '2023-10-16',
    }

    response = client.post(url, data=json.dumps(new_data), content_type='application/json')

    # Assert that the response status code is 201 Created
    assert response.status_code == status.HTTP_201_CREATED

    # check the response data if you expect specific content.
    response_data = response.data
    assert response_data['name'] == new_data['name']


@pytest.mark.django_db
def test_book_serializer():
    # Create a book instance
    book = create_test_book()

    # Serialize the book using BookSerializer
    serializer = BookSerializer(book)

    # Assert that the serialized data matches the expected data
    assert serializer.data['name'] == book.name
    assert serializer.data['author'] == book.author
    assert serializer.data['year'] == book.year
    assert serializer.data['short_description'] == book.short_description


@pytest.mark.django_db
def create_test_book():
    return Book.objects.create(
        name='Test Book',
        author='Test Author',
        year=2022,
        short_description='A test book for testing.',
        long_description='Long description for testing.',
        date_of_last_reading='2023-01-01',
    )


@pytest.mark.django_db
def test_book_detail_serializer():
    # Create a book instance
    book = create_test_book()

    # Serialize the book using BookDetailSerializer
    serializer = BookDetailSerializer(book)

    assert serializer.data['name'] == book.name
    assert serializer.data['author'] == book.author
    assert serializer.data['year'] == book.year
    assert serializer.data['short_description'] == book.short_description
    assert serializer.data['long_description'] == book.long_description
    assert serializer.data['date_of_last_reading'] == str(book.date_of_last_reading)


@pytest.mark.django_db
def test_book_detail_view_GET():
    # Create a test book
    book = create_test_book()

    # Send a GET request to retrieve the book by ID
    response = client.get(reverse('book_details', args=[book.id]))

    # Assert that the response status code is 200 OK
    assert response.status_code == status.HTTP_200_OK

    # Assert that the response data matches the expected data
    serializer = BookDetailSerializer(book)
    assert response.data == serializer.data


@pytest.mark.django_db
def test_book_detail_view_PUT():
    # Create a test book
    book = create_test_book()

    # Data for the PUT request
    updated_data = {
        'name': 'Updated Book Name',
        'author': 'Updated Author',
        'year': 2023,
        'short_description': 'Updated description',
        'long_description': 'Updated long description',
        'date_of_last_reading': '2023-10-16',
    }

    # Send a PUT request to update the book by ID
    response = client.put(reverse('book_details', args=[book.id]), updated_data, format='json')

    # Assert that the response status code is 200 OK
    assert response.status_code == status.HTTP_200_OK

    # Reload the book from the database and assert that it has been updated
    book.refresh_from_db()
    assert book.name == updated_data['name']
    assert book.author == updated_data['author']
    assert book.year == updated_data['year']
    assert book.short_description == updated_data['short_description']
    assert book.long_description == updated_data['long_description']
    assert str(book.date_of_last_reading) == updated_data['date_of_last_reading']


@pytest.mark.django_db
def test_book_detail_view_DELETE():
    # Create a test book
    book = create_test_book()

    # Send a DELETE request to delete the book by ID
    response = client.delete(reverse('book_details', args=[book.id]))

    # Assert that the response status code is 204 No Content
    assert response.status_code == status.HTTP_204_NO_CONTENT

    # Assert that the book has been deleted from the database
    with pytest.raises(Book.DoesNotExist):
        book.refresh_from_db()
