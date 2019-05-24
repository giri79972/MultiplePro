from django.contrib import admin

# Register your models here.
from .models import Customer,Emp,Student
# Register your models here.

class AdminCustomer(admin.ModelAdmin):
    list_display = ['cname','sales']
class AdminEmp(admin.ModelAdmin):
    list_display = ['ename','sal']
class AdminStudent(admin.ModelAdmin):
    list_display = ['sname','marks']
admin.site.register(Customer,AdminCustomer)
admin.site.register(Emp,AdminEmp)
admin.site.register(Student,AdminStudent)
