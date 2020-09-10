from django.contrib import admin
from emp_app.models import Department,Roles,Employee,EmployeeAttendance
# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display=['dept_id','dept_name']

admin.site.register(Department,DepartmentAdmin)

class RolesAdmin(admin.ModelAdmin):
    list_display=['role_id','role_name']

admin.site.register(Roles,RolesAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['emp_id','emp_name','dept_name','role_name',]

admin.site.register(Employee,EmployeeAdmin)

class EmployeeAttendanceAdmin(admin.ModelAdmin):
    list_display=['id','emp_id','date','ispresent','status']

admin.site.register(EmployeeAttendance,EmployeeAttendanceAdmin)
