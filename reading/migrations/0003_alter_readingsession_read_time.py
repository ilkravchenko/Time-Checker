# Generated by Django 4.2.6 on 2023-10-15 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reading', '0002_alter_readingsession_ended_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readingsession',
            name='read_time',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
