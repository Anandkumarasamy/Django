# Generated by Django 3.1.1 on 2020-09-08 09:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_id', models.IntegerField(primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=100)),
                ('dept_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empManagementApp.department')),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('role_id', models.IntegerField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('ispresent', models.BooleanField()),
                ('status', models.CharField(max_length=100, null=True)),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empManagementApp.employee')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='role_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empManagementApp.roles'),
        ),
    ]
