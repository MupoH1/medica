from django.contrib import admin
from .forms import *
from metatags.admin import MetaTagInline


class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1
    classes = ['collapse']


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'interest', 'is_main', 'is_slide']
    list_editable = ['interest', 'is_main', 'is_slide']
    inlines = [NewsImageInline, MetaTagInline]

    class Meta:
        model = News


admin.site.register(News, NewsAdmin)
