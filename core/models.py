from django.db import models


# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year = models.IntegerField()
    short_description = models.CharField(max_length=500)
    long_description = models.CharField(max_length=1000)
    date_of_last_reading = models.DateField(auto_now=True)

    def __str__(self):
        return self.name + ' ' + self.author + ' ' + str(self.year)
