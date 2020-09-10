from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from empManagementApp.models import Employee,Department,Roles,EmployeeAttendance
from empManagementApp.serializers import DepartmentSerializer,RolesSerializer,EmployeeSerializer,EmpAttendanceSerializer
from datetime import datetime

@api_view(['GET', 'POST'])
def department_list(request):
    """
    List all code empManagementApp, or create a new empManagementApp.
    """
    if request.method == 'GET':
        department = Department.objects.all()
        serializer = DepartmentSerializer(department, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def department_detail(request, pk):
    """
    Retrieve, update or delete a code empManagementApp.
    """
    try:
        department=Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def employee_list(request):
    """
    List all code empManagementApp, or create a new empManagementApp.
    """
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, pk):
    """
    Retrieve, update or delete a code empManagementApp.
    """
    try:
        employee= Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def role_list(request):
    """
    List all code empManagementApp, or create a new empManagementApp.
    """
    if request.method == 'GET':
        role = Roles.objects.all()
        serializer = RolesSerializer(role, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RolesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def role_detail(request, pk):
    """
    Retrieve, update or delete a code empManagementApp.
    """
    try:
        role= Roles.objects.get(pk=pk)
    except Roles.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RolesSerializer(role)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RolesSerializer(role, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['GET', 'POST'])
def empAttendance_list(request):
    """
    List all code empManagementApp, or create a new empManagementApp.
    """
    if request.method == 'GET':
        empAttendance = EmployeeAttendance.objects.all()
        serializer = EmpAttendanceSerializer(empAttendance, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EmpAttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def empAttendance_detail(request, pk):
    """
    Retrieve, update or delete a code empManagementApp.
    """
    try:
        empAttendance= EmployeeAttendance.objects.get(pk=pk)
    except EmployeeAttendance.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            
            empAttendance= EmployeeAttendance.objects.filter(emp_id=pk,date__month=datetime.now().month)
        except EmployeeAttendance.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EmpAttendanceSerializer(empAttendance,many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmpAttendanceSerializer(empAttendance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        empAttendance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
