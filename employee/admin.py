from django.contrib import admin
from .models import *
from .forms import *


class EmployeeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Employee._meta.fields]

    class Meta:
        model = Employee


admin.site.register(Employee, EmployeeAdmin)
