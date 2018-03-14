from django.contrib import admin
from .models import *
from .forms import *
from metatags.admin import MetaTagInline

class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1


class NewsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in News._meta.fields]
    list_editable = ['interest', 'is_main', 'is_slide']
    inlines = [NewsImageInline, MetaTagInline]

    class Meta:
        model = News


admin.site.register(News, NewsAdmin)
