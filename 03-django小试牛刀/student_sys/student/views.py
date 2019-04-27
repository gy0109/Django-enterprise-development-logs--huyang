from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import get_template
from django.urls import reverse

# Create your views here.
from django.views import View

from .models import Student
from .forms import StudentForm


def index(request):
    # students = Student.objects.all()
    students = Student.get_all()           # 配合model中的get_all模块可以将获取数据逻辑封装到model层
    tem = get_template('index.html')

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # 管理器
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


class IndexView(View):
    tem = get_template('index.html')

    def get_context(self):
        # students = Student.objects.all()
        students = Student.get_all()  # 配合model中的get_all模块可以将获取数据逻辑封装到model层
        return students

    def get(self, request):
        form = StudentForm()
        students = self.get_context()
        return HttpResponse(self.tem.render(locals()))

    def post(self, request):
        students = self.get_context()
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
                # student.created_time = cleaned_data['created_time']  #  不可修改  不要写

                # student.save()
                form.save()  # 使用这个不需要指定字段
                return HttpResponseRedirect(reverse('index'))

        # context = {'students': students}
        # request_context = RequestContext(request)   # 渲染模版
        # request_context.push(context)      # 推送参数到模板        # 与csrf_token 对接时出错
        #
        # return HttpResponse(request_context, 'index.html')
        return HttpResponse(self.tem.render(locals()))

