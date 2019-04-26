from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import get_template
from django.urls import reverse

# Create your views here.


from .models import Student
from .forms import StudentForm


def index(request):
    students = Student.objects.all()
    tem = get_template('index.html')

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # cleaned_data = form.cleaned_data
            # student = Student()
            # student.name = cleaned_data['name']
            # student.sex = cleaned_data['sex']
            # student.profession = cleaned_data['profession']
            # student.email = cleaned_data['email']
            # student.qq = cleaned_data['qq']
            # student.phone = cleaned_data['phone']
            # student.status = cleaned_data['status']
            # student.created_time = cleaned_data['created_time']
            #
            # student.save()
            form.save()
            return HttpResponseRedirect(reverse('index'))

        else:
            form = StudentForm()
    return HttpResponse(tem.render(locals()))




