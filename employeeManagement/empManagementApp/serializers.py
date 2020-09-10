from rest_framework import serializers
from empManagementApp.models import * 

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department 
        fields = ['dept_id', 'dept_name']

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles 
        fields = ['role_id', 'role_name']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee 
        fields = ['emp_id', 'emp_name', 'dept_name', 'role_name']

class EmpAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeAttendance 
        fields = ['emp_id', 'date','ispresent','status']
