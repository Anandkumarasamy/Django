from django.contrib import admin
from test_app.models import Employee_detaile,Manage_details
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esalary','eaddress']

admin.site.register(Employee_detaile,EmployeeAdmin)

class ManagerAdmin(admin.ModelAdmin):
    list_display=['mno','mname','erepoting_id','msalary','maddress']

admin.site.register(Manage_details,ManagerAdmin)
