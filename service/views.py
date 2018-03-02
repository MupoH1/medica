from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from department.models import Department
from .models import *
import json
from django.core import serializers


def price_list(request):
    data = request.POST
    service_id = data.get("service_id")
    department_id = data.get("department_id")
    data = list(PriceList.objects.filter(service_id=service_id, department_id=department_id).all())
    json_data = serializers.serialize('json', data)
    return HttpResponse(json_data, content_type='application/json')
