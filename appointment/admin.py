from django.contrib import admin
from .models import *
from .forms import *


class AppointmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Appointment._meta.fields]

    class Meta:
        model = Appointment


admin.site.register(Appointment, AppointmentAdmin)
