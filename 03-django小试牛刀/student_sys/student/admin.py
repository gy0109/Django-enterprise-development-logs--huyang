from django.contrib import admin
from .models import Student
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'profession', 'email', 'qq', 'phone', 'status', 'created_time')
    list_filter = ('sex', 'status', 'created_time')    # 侧边栏过滤器
    search_fields = ('name', 'profession')
    # fieldsets = (
    #     (None, {
    #         'fields': (
    #             'name',
    #             ('sex', 'profession'),
    #             ('email', 'qq', 'phone'),
    #             'status',
    #              )
    #     }),
    # )


# 注册admin
admin.site.register(Student, StudentAdmin)
