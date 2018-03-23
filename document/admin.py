from django.contrib import admin

from document.models import Document


class DocumentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Document._meta.fields]

    class Meta:
        model = Document


admin.site.register(Document, DocumentAdmin)
