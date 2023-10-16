# Generated by Django 4.2.6 on 2023-10-15 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reading', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readingsession',
            name='ended_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='readingsession',
            name='read_time',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='readingsession',
            name='started_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
