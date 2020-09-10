from django.urls import path
from empManagementApp import views

urlpatterns = [
    path('empManagementApp/employee', views.employee_list),
    path('empManagementApp/employee/<int:pk>/', views.employee_detail),
    path('empManagementApp/department', views.department_list),
    path('empManagementApp/department/<int:pk>/', views.department_detail),
    path('empManagementApp/role', views.role_list),
    path('empManagementApp/role/<int:pk>/', views.role_detail),
    path('empManagementApp/attendance', views.empAttendance_list),
    path('empManagementApp/attendance/<int:pk>/', views.empAttendance_detail),
]
