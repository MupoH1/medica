from django.contrib import admin
from .models import *
from .forms import *


class DocumentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Document._meta.fields]

    class Meta:
        model = Document


admin.site.register(Document, DocumentAdmin)
