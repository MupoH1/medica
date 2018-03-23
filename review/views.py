from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from appointment.forms import AppointmentForm
from department.models import Department
from review.forms import ReviewForm
from .models import *


def reviews(request):
    reviews_set = Review.objects.filter(is_active=True).order_by('date')
    department_set = Department.objects.all()

    review_form = ReviewForm(request.POST or None)
    if request.method == 'POST' and review_form.is_valid():
        review_form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    appointment_form = AppointmentForm(request.POST or None)
    if request.method == 'POST' and appointment_form.is_valid():
        appointment_form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    paginator = Paginator(reviews_set, 4, orphans=2)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, 'reviews.html', {"articles": articles,
                                            "review_form": review_form,
                                            'appointment_form': appointment_form,
                                            'departments': department_set})
