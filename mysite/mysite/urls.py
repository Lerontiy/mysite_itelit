"""mysite URL Configuration

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
from django.urls import re_path, path
from django.contrib import admin
from mysite import views
from html import *

urlpatterns = [
    re_path(r'^admin', admin.site.urls),
    re_path(r'^hello', views.hello),
    re_path(r'^time/plus/(\d+)', views.time_plus),
    re_path(r'^time$', views.time),
    re_path(r'^students$', views.students),
    re_path(r'^products', views.products),
    re_path(r'^progress', views.progress),
    re_path(r'^informatic', views.informatic),
    re_path(r'^sinformatic', views.sinformatic),
    re_path(r'^propusk', views.propusk),
    re_path(r'^better', views.better),
    re_path(r'^studentsView', views.studentsView),
    re_path(r'^uch$', views.uch),
    re_path(r'^uch_rev$', views.uch_rev),
    re_path(r'^uch_ost$', views.uch_ost),
    re_path(r'^uch_find$', views.uch_find),
    re_path(r'^uch_add$', views.uch_add),
    re_path(r'^auto$', views.auto),
    re_path('', views.no_urls),
]
