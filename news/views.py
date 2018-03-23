from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render

from appointment.forms import AppointmentForm
from department.models import Department
from .models import *


def news(request):
    appointment_form = AppointmentForm(request.POST or None)
    if request.method == 'POST' and appointment_form.is_valid():
        appointment_form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    news_set = News.objects.all().order_by('-interest', 'date')
    department_set = Department.objects.all()

    paginator = Paginator(news_set, 6, orphans=3)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, 'news.html', {"articles": articles, 'departments': department_set})


def text_page(request, news_id):
    appointment_form = AppointmentForm(request.POST or None)
    if request.method == 'POST' and appointment_form.is_valid():
        appointment_form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    departments = Department.objects.all()
    article = News.objects.get(id=news_id)
    artlist = list(News.objects.order_by('date'))
    ind = artlist.index(article)
    try:
        next_article = artlist.pop(ind+1)
    except IndexError:
        next_article = News.objects.order_by('date').first()

    try:
        previous_article = artlist.pop(ind-1)
    except IndexError:
        previous_article = News.objects.order_by('date').last()

    return render(request, 'text-page.html', locals())
