from django.http import HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from appointment.forms import AppointmentForm
from department.models import Department
from doctor_card.models import Doctor
# from index.models import Slide
from news.models import News


def index(request):

    appointment_form = AppointmentForm(request.POST or None)

    if request.method == 'POST' and appointment_form.is_valid():
        appointment_form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    doctors_set = Doctor.objects.order_by('?')[:6]
    department_set = Department.objects.filter(is_index_active=True)
    news_set = News.objects.filter(is_main=True).order_by('-interest', '?')[:3]

    slides = News.objects.filter(is_slide=True).order_by('-interest')

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

    return render(request, 'index.html', {"departments": department_set, "slides": slides,
                                          "doctors": doctors, "articles": news_set})
