from django.contrib import admin


# 创建admin基类   方便所有的 app.admin 使用
class BaseOwnerAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # request请求对象 obj当前要保存的对象 form form表单对象 change本次修改是更新还是第一次提交
        obj.owner = request.user  # 用户   未登录的时候是匿名用户
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):  # 展示自己的标签
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)
