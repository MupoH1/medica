from django.contrib import admin

from service.models import Service
from .models import *
from doctor_card.models import Doctor


class SlideAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Slide._meta.fields]


    class Meta:
        model = Slide


admin.site.register(Slide, SlideAdmin)
