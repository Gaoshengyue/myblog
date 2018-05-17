"""myblog URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from app01 import views
from myblog import settings
from django.views.static import  serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^index/(?P<name>\w+)/(?P<id>\d+)',views.index),
    url(r'^write/', views.write),
    url(r'^article_list/', views.article_list),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^login/', views.login),
    url(r'^add_tag/', views.add_tag),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^search/', views.search),
    url(r'^notfound/', views.notfound),
    url(r'^media/(?P<path>.*)$',serve,{"document_root":settings.MEDIA_ROOT}),
    url(r'^upload_img/', views.upload_img),
    url(r'^symoon/', views.symoon),

]
