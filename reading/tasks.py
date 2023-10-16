# from django.utils.timezone import now
# from celery import shared_task
# from datetime import datetime, timedelta
# from .models import ReadingSession
#
#
# @shared_task
# def update_reading_statistics(user_id):
#     user = ReadingSession.objects.filter(user=user_id)
#     today = now()
#     last_7_days = today - timedelta(days=7)
#     last_30_days = today - timedelta(days=30)
#
#     # Отримати статистику читання за останні 7 днів і 30 днів (припустимо, що в у вас є метод для цього)
#     statistics_7_days = user.get_reading_statistics(last_7_days, today)
#     statistics_30_days = user.get_reading_statistics(last_30_days, today)
#
#     # Зберегти статистику в профіль користувача
#     user.reading_statistics_7_days = statistics_7_days
#     user.reading_statistics_30_days = statistics_30_days
#     user.save()
