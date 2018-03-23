from django.contrib import admin

from .models import *
from employee.models import Doctor
from metatags.admin import MetaTagInline


class DoctorInline(admin.TabularInline):
    model = Doctor
    extra = 1
    classes = ['collapse']


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'short_name', 'consult_price', 'consult_doctor', 'is_index_active']
    list_editable = ['name', 'short_name', 'consult_price', 'consult_doctor', 'is_index_active']
    inlines = [DoctorInline, MetaTagInline,]

    class Meta:
        model = Department


admin.site.register(Department, DepartmentAdmin)
