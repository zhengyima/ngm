"""ngm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import view

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^near',view.near),
    url(r'^path',view.path),
    url(r'^find_path',view.find_path),
    url(r'^find_near',view.find_near),
    url(r'^getEdgeinfo',view.getEdgeinfo),
    url(r'^totalview$',view.totalview),
    url(r'^gettotalview$', view.gettotalview),
    url(r'^$',view.near)
]
