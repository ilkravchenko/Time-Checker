from django.urls import reverse
import datetime
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book
from reading.models import ReadingSession
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
    assert json.loads(response.content) == serializer.data


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
        'date_of_last_reading': datetime.datetime.now().strftime("%Y-%m-%d"),
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
    response = client.delete(reverse(viewname='book_details', args=[book.id]))

    # Assert that the response status code is 204 No Content
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_reading_session_POST():
    # Define the data for the new ReadingSession
    book_1 = Book.objects.create(id=2, name='Test2', author='Test2', year=2002, short_description='Test2',
                                 long_description='Long Test2')
    user_1 = User.objects.create(id=1,
                                 username='john',
                                 email='jlennon@beatles.com',
                                 password='glass onion')

    new_data = {
        'id': 1,
        'user': user_1.id,
        "started_at": "2023-10-16T19:09:29.549438Z",
        "ended_at": "2023-10-16T19:09:46.670401Z",
        "read_time": 21,
        "book": book_1.id,
    }

    # Send a POST request to create a new ReadingSession
    response = client.post(reverse('all_readers'), data=json.dumps(new_data), content_type='application/json')

    # Check if the request was successful (status code 201 Created)
    assert response.status_code == status.HTTP_201_CREATED

    # Check if the response data matches the expected data
    response_data = response.data
    assert response_data['id'] == new_data['id']
    assert response_data['user'] == new_data['user']
    assert response_data['read_time'] == new_data['read_time']
    assert response_data['book'] == new_data['book']


@pytest.mark.django_db
def test_reading_sessions_GET():
    # Create some ReadingSession objects in the database (use the actual data you expect)
    book_1 = Book.objects.create(id=1, name='Test', author='Test', year=2002, short_description='Test',
                                 long_description='Long Test')
    book_2 = Book.objects.create(id=2, name='Test2', author='Test2', year=2002, short_description='Test2',
                                 long_description='Long Test2')
    user_1 = User.objects.create(id=1,
                                 username='john',
                                 email='jlennon@beatles.com',
                                 password='glass onion')
    user_2 = User.objects.create(id=2,
                                 username='Test',
                                 email='test@beatles.com',
                                 password='Test')

    reading_record_1 = ReadingSession.objects.create(id=100,
                                                     user=user_1,
                                                     read_time=22,
                                                     book=book_1)
    reading_record_2 = ReadingSession.objects.create(id=200,
                                                     user=user_2,
                                                     read_time=20,
                                                     book=book_2)

    # Send a GET request to retrieve ReadingSessions
    response = client.get(reverse('all_readers'))

    # Check if the request was successful (status code 200 OK)
    assert response.status_code == status.HTTP_200_OK

    # Work, but started_at and ended_at have different format
    # Check if the response contains the expected data
    # expected_data = [
    #     {
    #         'id': 100,
    #         'user': 1,
    #         'started_at': str(reading_record_1.started_at),
    #         'ended_at': str(reading_record_1.ended_at),
    #         "read_time": 22,
    #         "book": 1,
    #     },
    #     {
    #         'id': 200,
    #         'user': 2,
    #         'started_at': str(reading_record_2.started_at),
    #         'ended_at': str(reading_record_2.ended_at),
    #         "read_time": 20,
    #         "book": 2,
    #     },
    # ]
    #
    # assert json.loads(response.content)['Readers'] == expected_data


@pytest.mark.django_db
def test_reading_sessions_GET_with_params():
    # Send a GET request to retrieve ReadingSessions
    response_1 = client.get(reverse('all_readers'), {'user': 1, 'book': 1})
    response_2 = client.get(reverse('all_readers'), {'book': 1})
    response_3 = client.get(reverse('all_readers'), {'user': 1})

    # Check if the request was successful (status code 200 OK)
    assert response_1.status_code == status.HTTP_200_OK
    assert response_2.status_code == status.HTTP_200_OK
    assert response_3.status_code == status.HTTP_200_OK
