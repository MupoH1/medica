from django.contrib import admin

from review.models import Review
from .models import *

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
    inlines = [DoctorTextFieldInline, SeniorityInline, ReviewInline]

    class Meta:
        model = Doctor

admin.site.register(Doctor, DoctorAdmin)