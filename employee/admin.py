from django.contrib import admin
from metatags.admin import MetaTagInline
from review.models import Review
from .models import Employee
from employee.models import Seniority, DoctorTextField, Doctor


class EmployeeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Employee._meta.fields]
    list_editable = ['full_name', 'position', 'is_displayed']

    class Meta:
        model = Employee


class SeniorityInline(admin.TabularInline):
    model = Seniority
    extra = 1
    classes = ['collapse']


class DoctorTextFieldInline(admin.TabularInline):
    model = DoctorTextField
    extra = 1
    classes = ['collapse']


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    classes = ['collapse']


class DoctorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Doctor._meta.fields]
    list_editable = ['name', 'position', 'is_active']
    inlines = [DoctorTextFieldInline, SeniorityInline, ReviewInline, MetaTagInline]

    class Meta:
        model = Doctor


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Doctor, DoctorAdmin)
