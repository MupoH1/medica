from django.http import HttpResponseRedirect
from django.shortcuts import render

from about.models import WordRequisites
from appointment.forms import AppointmentForm
from department.models import Department
from employee.models import Employee



def contacts(request):
    appointment_form = AppointmentForm(request.POST or None)
    if request.method == 'POST' and appointment_form.is_valid():
        appointment_form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    requisites = WordRequisites.objects.get(is_actual=True)
    departments = Department.objects.all()
    director = Employee.objects.filter(position="DR").get()
    main_doctor = Employee.objects.filter(position="MD").get()
    administration = Employee.objects.filter(position="AD").all()
    return render(request, 'contacts.html', locals())
