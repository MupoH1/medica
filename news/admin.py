from django.contrib import admin
from .models import *
from .forms import *


class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1


class NewsTextFieldInline(admin.TabularInline):
    model = NewsTextField
    extra = 0


class NewsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in News._meta.fields]
    inlines = [NewsTextFieldInline, NewsImageInline]

    class Meta:
        model = News


admin.site.register(News, NewsAdmin)
