from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Count

from appointment.forms import AppointmentForm
from employee.models import Doctor
from news.models import News
from service.models import Service, ExcellPrice
from .models import Department


def services(request):
    appointment_form = AppointmentForm(request.POST or None)
    if request.method == 'POST' and appointment_form.is_valid():
        appointment_form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    departments = Department.objects.all()

    return render(request, 'services.html', locals())


def department(request, department_id):
    appointment_form = AppointmentForm(request.POST or None)
    if request.method == 'POST' and appointment_form.is_valid():
        appointment_form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    current_department = Department.objects.get(id=department_id)
    doctors_set = Doctor.objects.filter(department=current_department)
    department_set = Department.objects.all()
    news_set = News.objects.all().order_by('-interest', '?')[:3]

    current_services_ids = current_department.pricelist_set.values_list('service', flat=True).annotate(n=Count("id"))[::1]
    current_services = Service.objects.filter(id__in=current_services_ids)

    doctors = get_doctor_pairs(doctors_set)
    excell_price = ExcellPrice.objects.get(is_actual=True)

    return render(request, 'department.html', {"department": current_department,
                                               "id": department_id,
                                               "services": current_services,
                                               "departments": department_set,
                                               "doctors": doctors,
                                               "articles": news_set,
                                               "price_file": excell_price})


def get_doctor_pairs(doctors_set):
    doctors = []
    doctors_pair = []
    i = 0
    for item in doctors_set:
        doctors_pair.append(item)
        i += 1
        if i == 2:
            i = 0
            doctors.append(list(doctors_pair))
            doctors_pair.clear()
    if doctors_set.count() % 2 != 0:
        doctors.append(list(doctors_pair))
    return doctors

