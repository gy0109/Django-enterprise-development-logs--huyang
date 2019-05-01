from django.contrib import admin
from django.contrib.auth import get_permission_codename
from django.urls import reverse
from django.utils.html import format_html

from .models import Tag, Category, Post
from .adminforms import PostAdminForm
from typeidea.custom_site import custom_site
# Register your models here.


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')

    def save_model(self, request, obj, form, change):
        # request请求对象 obj当前要保存的对象 form form表单对象 change本次修改是更新还是第一次提交
        obj.owner = request.user    # 用户   未登录的时候是匿名用户
        return super(TagAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):      # 展示自己的标签
        qs = super(TagAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)


class PostInline(admin.TabularInline):   # stackInline样式不同
    # 伪需求 适合字段较少的model
    fields = ('title', 'descripition')    # 指定相互关联编辑的字段   标题和摘要
    extra = 1     # 控制额外的几个
    model = Post  # 指定model类型


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_nav', 'created_time')
    fields = ('name', 'status', 'is_nav')

    inlines = [PostInline]      # 关联模型编辑的需求

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):   # 展示自己的分类
        qs = super(CategoryAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)


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
    # fields = (('title', 'category'),       # 限定要展示的字段， 配置展示字段的顺序
    #           'status', 'descripition', 'content', 'tag')
    fieldsets = (           # 控制布局 要求的格式是两个元素的tuple的list  （当前模板的名称， 元素当前板块的描述、字段和样式配置）
        ('基础配置', {
            # 'descripition': '基础配置描述',
            'fields': (
                ('title', 'category'),
                'status',
            ),
        }),
        ('内容', {
            'fields': (
                'descripition',
                'content',
            ),
        }),
        ('额外信息', {
            'classes': ('collapse',),    # classes的作用是给要配置的模板加上一些css属性默认支持collapse和wide
            'fields': ('tag',)
        }),
    )

    list_display_links = []  # 配置那些字段为链接（点击可进入文章详情页面）
    # list_filter = ['category']   # 页面过滤器  需要通过哪些字段过滤列表页
    list_filter = [CategoryOwnerFilter]    # 页面过滤器  展示自己定义的  不展示别人定义的
    search_fields = ['title', 'category__name']   # 配置搜索字段
    actions_on_bottom = True    # 是否展示在页面底部
    actions_on_top = True       # 是否展示在顶部
    save_on_top = True          # 保存  编辑 编辑并新建

    form = PostAdminForm             # 将字段修改成testare组件类型

    # exclude = ['owner']         # 字段不展示

    # filter_horizontal = ('tags', )     # 横向展示的字段
    # filter_vertical = ('tags', )       # 纵向展示的字段

    def operator(self, obj):
        #
        return format_html('<a href="{}">编辑</a>', reverse('cus_admin:blog_post_change', args=(obj.id,)))

    operator.short_description = '操作'    # 指定表头的展示文案

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)

    class Media:   # 自定义静态文件   若果是项目有的可以直接写项目绝对路径
        css = {
            'all': {'https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css'}
        }

        js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js')

    # PERMISSION_API = '单点登录的url'
    #
    # def has_add_permission(self, request):
    #     opts = self.opts
    #     codename = get_permission_codename('add', opts)
    #     perm_code = '%s: %s' % (opts.app_model, codename)
    #     resp = request.get(PERMISSION_API.format(request.user.username, perm_code))
    #     if resp.status.code == 200:
    #         return True
    #     else:
    #         return False


admin.site.register(Tag, TagAdmin, site=custom_site)
admin.site.register(Category, CategoryAdmin, site=custom_site)
admin.site.register(Post, PostAdmin, site=custom_site)
