from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

from appointment.forms import AppointmentForm
from department.models import Department
from employee.models import Doctor
from news.models import News


def index(request):

    appointment_form = AppointmentForm(request.POST or None)
    if request.method == 'POST' and appointment_form.is_valid():
        appointment_form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    doctors_set = Doctor.objects.order_by('?')[:6]
    department_set = Department.objects.all()
    department_isindex_set = Department.objects.filter(is_index_active=True)
    news_set = News.objects.filter(is_main=True).order_by('-interest', '?')[:3]

    slides = News.objects.filter(is_slide=True).order_by('-interest')

    doctors = get_doctor_pairs(doctors_set)

    return render(request, 'index.html', {"departments": department_set, "slides": slides,
                                          "doctors": doctors, "articles": news_set,
                                          "index_departments": department_isindex_set})


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


def handler404(request):
    departments = Department.objects.all()
    doctors = Doctor.objects.filter(is_active=True)
    news = News.objects.all()

    response = render_to_response('404.html', {"departments": departments, "doctors": doctors, "news": news})
    response.status_code = 404
    return response


def handler500(request):
    departments = Department.objects.all()
    doctors = Doctor.objects.filter(is_active=True)
    news = News.objects.all()

    response = render_to_response('404.html', {"departments": departments, "doctors": doctors, "news": news})
    response.status_code = 404
    return response
