from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.template import RequestContext

from department.models import Department
from .models import *


def faq(request, department_id=None):
    if department_id is None:
        department_id = Department.objects.all()[0].id

    departments = Department.objects.all()

    questions = Question.objects.filter(department_id=department_id).all()
    paginator = Paginator(questions, 9, orphans=3)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, 'faq.html', {"articles": articles, "departments": departments})
