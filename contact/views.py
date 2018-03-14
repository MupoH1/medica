from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import QuerySet, Count
from django.http import HttpResponseRedirect
from django.shortcuts import render

from employee.models import Employee
from .models import *


def contacts(request):
    director = Employee.objects.filter(position="DR").get()
    main_doctor = Employee.objects.filter(position="MD").get()
    administration = Employee.objects.filter(position="AD").all()
    return render(request, 'contacts.html', locals())
