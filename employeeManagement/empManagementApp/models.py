from django.db import models
from datetime import date

# Create your models here.
class Department(models.Model):
    dept_id=models.IntegerField(primary_key=True)
    dept_name=models.CharField(max_length=100,unique = True)
    def __str__(self):
        return self.dept_name

class Roles(models.Model):
    role_id=models.IntegerField(primary_key=True)
    role_name=models.CharField(max_length=100,unique = True)
    def __str__(self):
        return self.role_name

class Employee(models.Model):
    emp_id=models.IntegerField(primary_key=True)
    emp_name=models.CharField(max_length=100)
    dept_name=models.ForeignKey(Department,on_delete = models.CASCADE)
    #dept_Name=models.CharField(max_length=100,unique = True)
    role_name=models.ForeignKey(Roles,on_delete = models.CASCADE)
    #role_name=models.CharField(max_length=100,unique = True)
    def __int__(self):
        return self.emp_id

class EmployeeAttendance(models.Model):
    emp_id=models.ForeignKey(Employee,on_delete = models.CASCADE)
    date = models.DateField(("Date"), default=date.today)
    ispresent= models.BooleanField()
    status=models.CharField(max_length=100,blank=True,null=True)
    def __int__(self):
        return self.emp_id
