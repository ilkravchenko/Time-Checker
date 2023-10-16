# from .tasks import update_reading_statistics
from django.shortcuts import render
from django.utils.timezone import now
from .models import ReadingSession
from core.models import Book
import datetime
import requests
from django.contrib.auth.decorators import login_required
from .helpers import get_book, do_chart, create_new_reading_session, save_object

from django.db.models import Sum


# view for reading
@login_required(login_url='login')
def reading(request):
    response = requests.get('http://127.0.0.1:8000/books/')
    if request.method == 'GET':
        context = {
            'required': True,
            'books': response.json().get("Books"),
            'action': 'Choose your book for reading and start read!',
        }

        return render(request, template_name='reading/start-reading.html', context=context)

    if request.method == 'POST':
        data = request.POST
        action = data.get("follow")

        if action == "start":
            book = get_book(data=data, num_book="book")

            response = requests.get(f'http://127.0.0.1:8000/books/{book}')
            book_for_read = Book.objects.get(pk=book)

            # check for start reading same book
            try:
                check_same_book = ReadingSession.objects.get(user=request.user.id, book=book_for_read, read_time=None)

                # end reading one book and start new one
                if book_for_read.name == check_same_book.book.name:
                    context = {
                        'books': response.json(),
                        'action': 'You can\'t start read same book',
                        'follow': action,
                    }
                    return render(request, template_name='reading/start-reading.html', context=context)
                elif book_for_read.id != check_same_book.book.id:
                    check_same_book.read_time = (check_same_book.ended_at - check_same_book.started_at) // datetime.timedelta(
                        minutes=1)
                    check_same_book.save()

                    save_object(database=ReadingSession, user=request.user, read_time=None, book=book_for_read)

                    context = {
                        'books': response.json(),
                        'action': 'Go read your book!!',
                        'follow': action,
                    }
                    return render(request, template_name='reading/start-reading.html', context=context)

            except ReadingSession.DoesNotExist:
                try:
                    save_object(database=ReadingSession, user=request.user, read_time=None)
                    # update_reading_statistics.delay(request.user)
                except AttributeError:
                    pass

                create_new_reading_session(database=ReadingSession, book_for_read=book_for_read, request=request)

                context = {
                    'books': response.json(),
                    'action': 'Go read your book!!',
                    'follow': action,
                }
                return render(request, template_name='reading/start-reading.html', context=context)

        elif action == "end":
            save_object(database=ReadingSession, user=request.user, read_time=None)
            # update_reading_statistics.delay(request.user)

            context = {
                'required': True,
                'books': response.json().get("Books"),
                'action': 'Choose your book for reading and start read!',
            }

            return render(request, template_name='reading/start-reading.html', context=context)


# view for user statistics
def statistics(request):
    all_user_statistics = ReadingSession.objects.filter(user=request.user.id)
    today_user_statistics = ReadingSession.objects.filter(user=request.user.id,
                                                          started_at__gte=now().replace(hour=0, minute=0, second=0),
                                                          ended_at__lte=now().replace(hour=23, minute=59, second=59))

    total_books = len(set(all_user_statistics.values_list('book', flat=True)))
    total_minutes = sum(all_user_statistics.values_list('read_time', flat=True))

    today_books = len(set(today_user_statistics.values_list('book', flat=True)))
    today_minutes = sum(today_user_statistics.values_list('read_time', flat=True))

    list_all_book_stat = all_user_statistics.values('book__name').annotate(
        count_total=Sum('read_time'),
    )
    list_today_book_stat = today_user_statistics.values('book__name').annotate(
        count_total=Sum('read_time'),
    )

    # chart for list_all_book_stat
    graphic_1 = do_chart(list_all_book_stat, name_of_chart='All Minutes by Books')

    # chart for list_today_book_stat
    graphic_2 = do_chart(list_today_book_stat, name_of_chart="Today Minutes by Books")

    context = {
        'today_books': today_books,
        'total_books': total_books,
        'today_minutes': today_minutes,
        'total_minutes': total_minutes,
        'list_all_book_stat': graphic_1,
        'list_today_book_stat': graphic_2,
    }
    return render(request, template_name='reading/statistics.html', context=context)
