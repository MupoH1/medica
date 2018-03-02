from django.contrib import admin
from import_export import admin as ieadmin

from .models import *


class PriceListInline(admin.TabularInline):
    model = PriceList
    extra = 1


class ServiceAdmin(ieadmin.ImportExportModelAdmin):
    list_display = [field.name for field in Service._meta.fields]
    inlines = [PriceListInline]


    class Meta:
        model = Service, PriceList


class PriceListAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PriceList._meta.fields]

    class Meta:
        model = PriceList


admin.site.register(Service, ServiceAdmin)
admin.site.register(PriceList, PriceListAdmin)
