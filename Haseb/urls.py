"""Haseb URL Configuration

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
from Search import views

urlpatterns = [
    url(r'^$', views.varse, name='index'),
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^search/$', views.SearchPageView.as_view(), name='search'),
    #url(r'^test/$', views.varse, name='test'),
    url(r'^search/poetry/$', views.SearchPageView.PoertyPageView.as_view(), name='poetry'),
    url(r'^admin/', admin.site.urls),
]
