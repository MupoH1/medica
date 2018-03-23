from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

from department.models import Department
from employee.models import Doctor
from news.models import News


class DepartmentSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1

    def items(self):
        return Department.objects.all()

    def lastmod(self, obj):
        return obj.updated


class DoctorSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1

    def items(self):
        return Doctor.objects.all()

    def lastmod(self, obj):
        return obj.updated


class NewsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return News.objects.all()

    def lastmod(self, obj):
        return obj.date


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['about', 'contacts', 'doctors', 'documents', 'faq', 'index', 'reviews', 'services']

    def location(self, item):
        return reverse(item)

