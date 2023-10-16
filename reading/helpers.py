import matplotlib.pyplot as plt
from django.utils.timezone import now
import datetime
from io import BytesIO
import base64


# function to get book number
def get_book(data, num_book):
    try:
        return int(data.get(num_book))
    except Exception as e:
        raise e


# function to add value labels
def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha='center')


def do_chart(list_of_data, name_of_chart):
    x = [book_name['book__name'] for book_name in list_of_data]
    y = [book_name['count_total'] for book_name in list_of_data]

    # setting figure size by using figure() function
    plt.figure(figsize=(10, 5))

    # making the bar chart on the data
    plt.bar(x, y)

    # calling the function to add value labels
    addlabels(x, y)

    # giving title to the plot
    plt.title(name_of_chart)

    # giving X and Y labels
    plt.xlabel("Name of the book")
    plt.ylabel("Minutes")

    # visualizing the plot
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return graphic


# create new object in ReadingSession
def create_new_reading_session(database, book_for_read, request):
    new_session = database()
    new_session.user = request.user
    new_session.book = book_for_read
    new_session.save()


# save object in ReadingSession
def save_object(database, user, read_time, book=None):
    if book == None:
        new_session = database.objects.filter(user=user, read_time=read_time).first()
    else:
        new_session = database.objects.filter(user=user, read_time=read_time, book=book).first()
    new_session.ended_at = now()
    new_session.read_time = (new_session.ended_at - new_session.started_at) // datetime.timedelta(minutes=1)
    new_session.save()
