from django.contrib import admin

from .models import *

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'contact', 'address']

class ShiftAdmin(admin.ModelAdmin):
    list_display = ['name', 'employee', 'start_time', 'end_time', 'date']

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Shift, ShiftAdmin)