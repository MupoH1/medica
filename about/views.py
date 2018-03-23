from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render

from appointment.forms import AppointmentForm
from department.models import Department
from .models import *


def about(request):
    appointment_form = AppointmentForm(request.POST or None)
    if request.method == 'POST' and appointment_form.is_valid():
        appointment_form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    departments = Department.objects.all()
    article = About.objects.get(is_active=True)

    return render(request, 'about.html', locals())

