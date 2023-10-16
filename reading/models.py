from django.utils.timezone import now
from django.db import models
from core.models import Book
from django.contrib.auth.models import User


# Create your models here.
class ReadingSession(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    started_at = models.DateTimeField(auto_now_add=True, blank=False)
    ended_at = models.DateTimeField(auto_now=True, blank=True)
    read_time = models.IntegerField(null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, blank=False)
    # reading_statistics_7_days = models.IntegerField(blank=True)
    # reading_statistics_30_days = models.IntegerField(blank=True)

    def __str__(self):
        return str(self.user) + ' ' + str(self.book)

    # def get_reading_statistics(self, days_of_statistics, today):
    #     user_statistics = ReadingSession.objects.filter(user=self.user,
    #                                                     started_at__gte=days_of_statistics.replace(hour=0, minute=0,
    #                                                                                                second=0),
    #                                                     ended_at__lte=now().replace(hour=23, minute=59,
    #                                                                                 second=59))
    #
    #     minutes = sum(user_statistics.values_list('read_time', flat=True))
    #
    #     return minutes
