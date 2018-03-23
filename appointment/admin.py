from django.contrib import admin
from .forms import *


class AppointmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Appointment._meta.fields]
    list_editable = ['full_name', 'phone_number', 'email']

    class Meta:
        model = Appointment


admin.site.register(Appointment, AppointmentAdmin)
