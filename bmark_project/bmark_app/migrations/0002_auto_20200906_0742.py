# Generated by Django 2.2.16 on 2020-09-06 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmark_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmark',
            old_name='date',
            new_name='Booking_date',
        ),
        migrations.AddField(
            model_name='customerbookmark',
            name='BookMark_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
