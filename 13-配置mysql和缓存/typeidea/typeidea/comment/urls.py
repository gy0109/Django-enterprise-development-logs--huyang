from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^comment/$', views.CommentView.as_view(), name='comment'),
]


