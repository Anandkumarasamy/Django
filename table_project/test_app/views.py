from django.shortcuts import render
from test_app.models import Employee_detaile,Manage_details
# Create your views here.
def home_page(request):
    return render(request,'test_app/home.html')

def Employee_page(request):
    employee_list=Employee_detaile.objects.all()
    my_dict={'Employee_list':employee_list}
    return render(request,'test_app/employee.html',my_dict)

def Manager_page(request):
    manager_list=Manage_details.objects.all()
    my_dict={'Manager_list':manager_list}
    return render(request,'test_app/manager.html',my_dict)
