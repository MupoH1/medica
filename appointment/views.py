from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.template import RequestContext

from department.models import Department
from .models import *
