from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render

from appointment.forms import AppointmentForm
from employee.models import Doctor
from department.models import *
from faq.forms import QuestionForm
from review.forms import ReviewForm


def doctors(request):
    appointment_form = AppointmentForm(request.POST or None)
    if request.method == 'POST' and appointment_form.is_valid():
        appointment_form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    departments = Department.objects.annotate(doctors_count=Count('doctor'))
    departments_one_doctor = departments.filter(doctors_count=1)
    departments_other = departments.exclude(doctors_count=1)
    return render(request, 'doctors.html', locals())


def doctor_card(request, doctor_id):
    appointment_form = AppointmentForm(request.POST or None)
    if request.method == 'POST' and appointment_form.is_valid():
        appointment_form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    review_form = ReviewForm(request.POST or None)
    if request.method == 'POST' and review_form.is_valid():
        review_form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    question_form = QuestionForm(request.POST or None)
    if request.method == 'POST' and question_form.is_valid():
        question_form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    doctor = Doctor.objects.get(id=doctor_id)
    reviews_set = doctor.review_set.filter(is_active=True).order_by('date')
    department_set = Department.objects.all()

    paginator = Paginator(reviews_set, 4)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, 'doctor-card.html', {"articles": articles, "doctor": doctor,
                                                "departments": department_set, "review_form": review_form,
                                                'question_form': question_form})
