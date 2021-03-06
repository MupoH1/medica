"""medica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView

from .sitemaps import DepartmentSitemap, DoctorSitemap, NewsSitemap, StaticViewSitemap

handler404 = 'index.views.handler404'
handler500 = 'index.views.handler500'

sitemaps = {
            'department': DepartmentSitemap,
            'doctor': DoctorSitemap,
            'news': NewsSitemap,
            'static': StaticViewSitemap
            }

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^', include('news.urls')),
    url(r'^', include('review.urls')),
    url(r'^', include('doctor_card.urls')),
    url(r'^', include('service.urls')),
    url(r'^', include('department.urls')),
    url(r'^', include('faq.urls')),
    url(r'^', include('index.urls')),
    url(r'^', include('document.urls')),
    url(r'^', include('contacts.urls')),
    url(r'^', include('about.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
