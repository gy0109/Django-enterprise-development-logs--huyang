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


class CategoryOwnerFilter(admin.SimpleListFilter):
    """自定义过滤器只显示房钱用户的分类"""
    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        catagory_id = self.value()
        if catagory_id:
            return queryset.filter(catagory_id=self.value())

        return queryset


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'created_time', 'operator', 'owner')   # 配置列表页面显示什么字段
    fields = (('title', 'category'),
              'status', 'descripition', 'content', 'tag')
    list_display_links = []  # 配置那些字段为链接（点击可进入文章详情页面）
    # list_filter = ['category']   # 页面过滤器  需要通过哪些字段过滤列表页
    list_filter = [CategoryOwnerFilter]    # 页面过滤器  展示自己定义的  不展示别人定义的
    search_fields = ['title', 'category__name']   # 配置搜索字段
    actions_on_bottom = True    # 是否展示在页面底部
    actions_on_top = True       # 是否展示在顶部
    save_on_top = True          # 保存  编辑 编辑并新建

    def operator(self, obj):
        return format_html('<a href="{}">编辑</a>', reverse('admin:blog_post_change', args=(obj.id,)))

    operator.short_description = '操作'    # 指定表头的展示文案

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)


# class PostOwnerFilter(admin.SimpleListFilter):
#     """自定义过滤器只显示房钱用户的分类"""
#     title = '文章过滤器'
#     parameter_name = 'owner_post'
#
#     def lookups(self, request, model_admin):
#         return Category.objects.filter(owner=request.user).values_list('id', 'title')
#
#     def queryset(self, request, queryset):
#         catagory_id = self.value()
#         if catagory_id:
#             return queryset.filter(catagory_id=self.value())
#
#         return queryset


admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
