from django.contrib import admin
from .forms import *


class QuestionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Question._meta.fields]
    list_editable = ['curator', 'department', 'news']


    class Meta:
        model = Question


admin.site.register(Question, QuestionAdmin)
