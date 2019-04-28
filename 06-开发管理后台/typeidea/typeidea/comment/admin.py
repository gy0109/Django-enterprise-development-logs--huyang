from django.contrib import admin
from .models import Comment


# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'status', 'email', 'content', 'created_time')
    fields = ('nickname', 'status')

    def save_model(self, request, obj, form, change):
        # request请求对象 obj当前要保存的对象 form form表单对象 change本次修改是更新还是第一次提交
        obj.owner = request.user  # 用户   未登录的时候是匿名用户
        return super(CommentAdmin, self).save_model(request, obj, form, change)


admin.site.register(Comment, CommentAdmin)

