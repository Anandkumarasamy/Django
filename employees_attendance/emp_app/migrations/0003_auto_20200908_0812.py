# Generated by Django 2.2.16 on 2020-09-08 08:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0002_auto_20200908_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeattendance',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='employeeattendance',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
