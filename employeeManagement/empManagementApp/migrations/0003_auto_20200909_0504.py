# Generated by Django 2.2.16 on 2020-09-09 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empManagementApp', '0002_auto_20200908_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='dept_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employeeattendance',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='roles',
            name='role_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
