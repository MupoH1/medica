from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import QuerySet, Count
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from department.models import *


def doctors(request):
    departments = Department.objects.annotate(doctors_count=Count('doctor'))
    departments_one_doctor = departments.filter(doctors_count=1)
    departments_other = departments.exclude(doctors_count=1)
    return render(request, 'doctors.html', locals())


def doctor_card(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    reviews_set = doctor.review_set.filter(is_active=True).order_by('date')

    paginator = Paginator(reviews_set, 4)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, 'doctor-card.html', {"articles": articles, "doctor": doctor})
