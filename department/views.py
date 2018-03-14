from django.http import HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.db.models import QuerySet, Count

from employee.models import Doctor
from news.models import News
from service.models import Service
from .models import Department


def services(request):
    department_set = Department.objects.all()

    return render(request, 'services.html', locals())


def department(request, department_id):
    current_department = Department.objects.get(id=department_id)
    doctors_set = Doctor.objects.filter(department=current_department)
    department_set = Department.objects.all()
    news_set = News.objects.all().order_by('-interest', '?')[:3]

    current_services_ids = current_department.pricelist_set.values_list('service', flat=True).annotate(n=Count("id"))[::1]
    current_services = Service.objects.filter(id__in=current_services_ids)

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

    return render(request, 'department.html', {"department": current_department,
                                               "id": department_id,
                                               "services": current_services,
                                               "departments": department_set,
                                               "doctors": doctors,
                                               "articles": news_set})
