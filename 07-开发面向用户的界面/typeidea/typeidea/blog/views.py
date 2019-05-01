from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

# Create your views here.


def post_list(request, category_id=None, tag_id=None):
    tem = get_template('list.html')
    name = 'post_list'
    return HttpResponse(tem.render(locals()))


def post_detail(request, post_id):
    tem = get_template('list.html')
    name = 'post_list'
    return HttpResponse(tem.render(locals()))

