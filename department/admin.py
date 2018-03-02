from django.contrib import admin

from .models import *
from doctor_card.models import Doctor
from metatags.admin import MetaTagInline


class DoctorInline(admin.TabularInline):
    model = Doctor
    extra = 1


class DepartmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Department._meta.fields]
    inlines = [DoctorInline, MetaTagInline,]


    class Meta:
        model = Department


admin.site.register(Department, DepartmentAdmin)
