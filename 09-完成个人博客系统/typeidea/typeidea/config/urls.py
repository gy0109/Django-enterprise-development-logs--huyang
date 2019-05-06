from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^links/$', views.LinksListView.as_view(), name='links')
]


