from rest_framework import serializers
from emp_app.models import EmployeeAttendance

class EmployeeAttendance_serializer(serializers.ModelSerializer):

    class Meta:
        model=EmployeeAttendance
        fields = ('emp_id','date','ispresent','status')
        #fields = '__all__'
