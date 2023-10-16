from django.db import models


# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=False)
    author = models.CharField(max_length=200, blank=False)
    year = models.IntegerField(blank=False)
    short_description = models.CharField(max_length=500, blank=False)
    long_description = models.CharField(max_length=1000, blank=False)
    date_of_last_reading = models.DateField(auto_now=True, blank=False)

    def __str__(self):
        return self.name + ' ' + self.author + ' ' + str(self.year)
