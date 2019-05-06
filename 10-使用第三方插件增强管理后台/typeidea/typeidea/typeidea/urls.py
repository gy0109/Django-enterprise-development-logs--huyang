"""typeidea URL Configuration

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
import xadmin
from .autocomplete import CategoryAutoComplete, TagAutoComplete
from typeidea.custom_site import custom_site

urlpatterns = [
    # url(r'^super_admin/', admin.site.urls, name='super_admin'),
    url(r'^super_xadmin/', xadmin.site.urls, name='super_xadmin'),
    url(r'^admin/', custom_site.urls, name='admin'),
    url(r'^', include('blog.urls')),
    url(r'^', include('config.urls')),
    url(r'^', include('comment.urls')),

    # 搜索框自动补全
    url(r'^categoryautocomplete/$', CategoryAutoComplete.as_view(), name='categoryautocomplete'),
    url(r'^tagautocomplete/$', TagAutoComplete.as_view(), name='tagautocomplete'),


]
