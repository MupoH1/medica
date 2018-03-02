from django.contrib import admin
from .models import *
from .forms import *


class QuestionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Question._meta.fields]

    class Meta:
        model = Question


admin.site.register(Question, QuestionAdmin)
