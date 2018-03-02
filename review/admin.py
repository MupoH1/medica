from django.contrib import admin
from .models import *


class ReviewAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Review._meta.fields]

    class Meta:
        model = Review


admin.site.register(Review, ReviewAdmin)
