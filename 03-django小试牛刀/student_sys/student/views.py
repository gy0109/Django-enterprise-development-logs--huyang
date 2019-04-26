from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template

from .models import Student


def index(request):
    students = Student.objects.all()
    tem = get_template('index.html')
    return HttpResponse(tem.render(locals()))
