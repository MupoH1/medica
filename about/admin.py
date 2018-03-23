from django.contrib import admin
from about.models import AboutImage, About, WordRequisites
from metatags.admin import MetaTagInline


class AboutImageInline(admin.TabularInline):
    model = AboutImage
    extra = 1
    classes = ['collapse']


class AboutAdmin(admin.ModelAdmin):
    list_display = [field.name for field in About._meta.fields]
    inlines = [AboutImageInline, MetaTagInline]

    class Meta:
        model = About


class WordRequisitesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in WordRequisites._meta.fields]
    list_editable = ['is_actual']

    class Meta:
        model = WordRequisites


admin.site.register(About, AboutAdmin)
admin.site.register(WordRequisites, WordRequisitesAdmin)
