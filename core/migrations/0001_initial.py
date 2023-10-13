# Generated by Django 4.2.6 on 2023-10-13 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('short_description', models.CharField(max_length=500)),
                ('long_description', models.CharField(max_length=1000)),
                ('date_of_last_reading', models.DateField(auto_now=True)),
            ],
        ),
    ]
