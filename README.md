
# Time checker

This project will track the time spent by a user reading a book. The user can start a reading session, finish it, and the system will store the duration of each session and the total reading time for each book.


## Run Locally

Clone the project

```bash
  git clone https://github.com/ilkravchenko/Time-Checker.git
```

Go to the project directory

```bash
  cd Time_Checker
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python manage.py runserver
```

Available Urls

```bash
    admin/ - admin page
    books/ - List all books
    books/<int:id>/ - list one book by id
    readers/ List all reading history
    readers/<int:id>/ list one record from reading history by id
    reading/ - main page for Time Checking
    reading/ statistics/ - Statistics for Users
    users/register/ - Registration
    users/login/ - Login
    users/logout/ - Logout
```


## Screenshots and Usage
This is a main page of Application where you can start and end reading your book, register and login, alse from here you can see statistics by clicking on button "Statistics". Also for best experience you can see the list of all books for reading.
![image](https://github.com/ilkravchenko/Time-Checker/assets/117378994/48bc2683-1130-45fe-aaa2-d8bcd4d68c33)

  - - - -
This is a main page of Application when you clicked start. After clicking you can see book which you choosed for reading. And now you can click end reading or start read other book, but here is a exceptions, because user can't start read same book and if choose other book the record from previos will save and start new record 
![image](https://github.com/ilkravchenko/Time-Checker/assets/117378994/b58c578b-99be-48b1-98bf-7750a0254a64)

  - - - -
This is a statistics page where users can see their statistics of reading, such as numbers of books and minutes, and dashboards of minutes by every readed book. 
![image](https://github.com/ilkravchenko/Time-Checker/assets/117378994/68cad926-1a07-4e47-8e7a-2a0d1564a863)
## API Reference

#### GET and POST all books

```http
  GET /books
  POST /books
```
![image](https://github.com/ilkravchenko/Time-Checker/assets/117378994/bfeb66b0-526f-46c5-a5be-7cd81efa9d2d)
#### GET, PUT and DELETE book

```http
  GET /books/${id}
  PUT /books/${id}
  DELETE /books/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int   ` | **Required**. Id of book to fetch |

![image](https://github.com/ilkravchenko/Time-Checker/assets/117378994/75933a7f-4ea2-4339-b1c3-73c78640cd9e)

#### GET and POST all reading records

```http
  GET /readers
  POST /readers
```
![image](https://github.com/ilkravchenko/Time-Checker/assets/117378994/8e2d26cd-6c73-4e5a-8c70-62348f4cd492)
#### GET, PUT and DELETE reading record

```http
  GET /readers/${id}
  PUT /readers/${id}
  DELETE /readers/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int   ` | **Required**. Id of reading record to fetch |

![image](https://github.com/ilkravchenko/Time-Checker/assets/117378994/8e87bcd7-7494-4863-be10-92999f4cabc5)




## Running Tests

To run tests, run the following command

```bash
  pytest
```

Using this command you can run 7 project's test and can see that these all tests were passed. All created tests are listed below:
* test_book_list_view_GET
* test_book_list_view_POST
* test_book_serializer
* test_book_detail_serializer
* test_book_detail_view_GET
* test_book_detail_view_PUT
* test_book_detail_view_DELETE

```bash
collected 7 items
core\tests.py .....                                       [100%]

====================== 7 passed in 2.10s =======================

```
