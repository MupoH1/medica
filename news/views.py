from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import *


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
