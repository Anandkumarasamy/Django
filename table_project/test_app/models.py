from django.db import models

# Create your models here.
class Employee_detaile(models.Model):
    eno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    esalary=models.FloatField()
    eaddress=models.TextField(max_length=200)

    def __str__(self):
        return self.ename

class Manage_details(models.Model):
    mno=models.IntegerField(primary_key=True)
    mname=models.CharField(max_length=100)
    erepoting_id=models.ForeignKey(Employee_detaile,on_delete = models.CASCADE)
    msalary=models.FloatField()
    maddress=models.TextField(max_length=200)

    def __str__(self):
        return self.mname
