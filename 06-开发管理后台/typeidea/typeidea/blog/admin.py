from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Tag, Category, Post

# Register your models here.


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')

    def save_model(self, request, obj, form, change):
        # request请求对象 obj当前要保存的对象 form form表单对象 change本次修改是更新还是第一次提交
        obj.owner = request.user    # 用户   未登录的时候是匿名用户
        return super(TagAdmin, self).save_model(request, obj, form, change)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_nav', 'created_time')
    fields = ('name', 'status', 'is_nav')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'created_time', 'operator')
    fields = (('title', 'category'),
              'status', 'descripition', 'content', 'tag')
    list_display_links = []
    list_filter = ['category']
    search_fields = ['title', 'category__name']
    actions_on_bottom = True
    actions_on_top = True
    save_on_top = True

    def operator(self, obj):
        return format_html('<a href="{}">编辑</a>',
        reverse('admin.blog_post_change', args=(obj.id,)))

    operator.short_description = '操作'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)


admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
