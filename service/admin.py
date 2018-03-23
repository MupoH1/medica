from django.contrib import admin
from import_export import admin as ieadmin

from .models import *


class PriceListInline(admin.TabularInline):
    model = PriceList
    extra = 1
    classes = ['collapse']


class ServiceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Service._meta.fields]
    list_editable = ['service_name']
    inlines = [PriceListInline]

    class Meta:
        model = Service


class ExcellPriceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ExcellPrice._meta.fields]
    list_editable = ['is_actual']

    class Meta:
        model = ExcellPrice


class PriceListAdmin(ieadmin.ImportExportModelAdmin):
    list_display = [field.name for field in PriceList._meta.fields]
    list_editable = ['item_name', 'item_price', 'item_time', 'service', 'department']

    class Meta:
        model = PriceList


admin.site.register(Service, ServiceAdmin)
admin.site.register(PriceList, PriceListAdmin)
admin.site.register(ExcellPrice, ExcellPriceAdmin)
