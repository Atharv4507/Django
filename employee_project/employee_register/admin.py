from django.contrib import admin
from employee_register.models import Position
from employee_register.models import Employee
from employee_register.models import Advertising
# Register your models here.

admin.site.register(Position)
admin.site.register(Employee)
admin.site.register(Advertising)