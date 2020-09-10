# Generated by Django 2.2.16 on 2020-09-05 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manage_details',
            fields=[
                ('mno', models.IntegerField(primary_key=True, serialize=False)),
                ('mname', models.CharField(max_length=100)),
                ('msalary', models.FloatField()),
                ('maddress', models.TextField(max_length=200)),
                ('erepoting_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.Employee_detaile')),
            ],
        ),
    ]
