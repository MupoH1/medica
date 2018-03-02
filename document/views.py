from django.http import HttpResponseRedirect
from django.shortcuts import render

from appointment.forms import AppointmentForm
from .models import *


def documents(request):
    documents_set = Document.objects.all()
    appointment_form = AppointmentForm(request.POST or None)
    if request.method == 'POST' and appointment_form.is_valid():
        appointment_form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request, 'documents.html', locals())
