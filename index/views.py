from django.http import HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from department.models import Department
from doctor_card.models import Doctor
from index.models import Slide
from news.models import News


def index(request):

    doctors_set = Doctor.objects.order_by('?')[:6]
    department_set = Department.objects.filter(is_index_active=True)
    news_set = News.objects.all().order_by('?')[:3]

    slides = Slide.objects.all()

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
