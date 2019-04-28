from django.contrib import admin
from .models import SiderBar, Link


# Register your models here.

class SiderBarAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_type', 'status', 'created_time')
    fields = ('title', 'status')

    def save_model(self, request, obj, form, change):
        # request请求对象 obj当前要保存的对象 form form表单对象 change本次修改是更新还是第一次提交
        obj.owner = request.user  # 用户   未登录的时候是匿名用户
        return super(SiderBarAdmin, self).save_model(request, obj, form, change)


class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'href', 'status', 'created_time')
    fields = ('title', 'status')

    def save_model(self, request, obj, form, change):
        # request请求对象 obj当前要保存的对象 form form表单对象 change本次修改是更新还是第一次提交
        obj.owner = request.user  # 用户   未登录的时候是匿名用户
        return super(LinkAdmin, self).save_model(request, obj, form, change)


admin.site.register(SiderBar, SiderBarAdmin)
admin.site.register(Link, LinkAdmin)
