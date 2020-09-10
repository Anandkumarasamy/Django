from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes,permission_classes
#from rest_framework.views import APIView
from rest_framework.decorators import api_view
from datetime import datetime
import json

from emp_app.models import EmployeeAttendance,Employee
from emp_app.serializers import EmployeeAttendance_serializer
# Create your views here.
'''@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def auth_view(request, format=None):
    content = {
        'user': unicode(request.user),  # `django.contrib.auth.User` instance.
        'auth': unicode(request.auth),  # None
    }
    return Response(content)'''

@api_view(['GET', 'POST'])
def employee_attendance_list(request):
    """
    List all code employee_attendance, or create a new employee_attendance.
    """
    if request.method == 'GET':
        emp_attend = EmployeeAttendance.objects.all()
        serializer = EmployeeAttendance_serializer(emp_attend, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EmployeeAttendance_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def employee_attendance_detail(request, emp_id, format=None):
    """
    Retrieve, update or delete a code employee_attendance.
    """
    try:
        emp_attendance = EmployeeAttendance.objects.filter(emp_id=emp_id,date__month=datetime.now().month)
    except EmployeeAttendance.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        #emp_attendance1=emp_attendance.objects.filter()
        serializer = EmployeeAttendance_serializer(emp_attendance,many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeeAttendance_serializer(emp_attendance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        EmployeeAttendance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
