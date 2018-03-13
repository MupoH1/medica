from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.template import RequestContext

from .models import *


# def landing(request):
#     name = 'Miron'
#     current_day = "16.10.2017"
#     form = SubscriberForm(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         print(request.POST)
#         print(form.cleaned_data)
#         data = form.cleaned_data
#         print(data['name'])
#
#         new_form = form.save()
#         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#
#     return render(request, 'landing/landing.html', locals())


def news(request):
    news_set = News.objects.all().order_by('-interest', 'date')

    paginator = Paginator(news_set, 6, orphans=3)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, 'news.html', {"articles": articles})


def text_page(request, news_id):
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
