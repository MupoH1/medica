from django.contrib import admin
from .models import *


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'date', 'doctor', 'is_active']
    list_editable = ['doctor', 'is_active']

    class Meta:
        model = Review


admin.site.register(Review, ReviewAdmin)
