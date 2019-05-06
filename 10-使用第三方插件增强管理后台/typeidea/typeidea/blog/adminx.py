from django.contrib import admin
import xadmin
from django.contrib.admin.models import LogEntry
from django.urls import reverse
from django.utils.html import format_html
from xadmin.layout import Row, Fieldset
from xadmin.filters import manager
from xadmin.filters import RelatedFieldSearchFilter
from .models import Tag, Category, Post
from .adminforms import PostAdminForm
from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin
# Register your models here.


class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')


class PostInline(admin.TabularInline):   # stackInline样式不同
    # 伪需求 适合字段较少的model
    fields = ('title', 'descripition')    # 指定相互关联编辑的字段   标题和摘要
    extra = 1     # 控制额外的几个
    model = Post  # 指定model类型


class CategoryAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'is_nav', 'created_time')
    fields = ('name', 'status', 'is_nav')

    inlines = [PostInline]      # 关联模型编辑的需求


class CategoryOwnerFilter(RelatedFieldSearchFilter):
    @classmethod
    def test(cls, field, request, params, model, admin_view, field_path):
        return field.name == 'category'

    def __init__(self, field, request, params, model, admin_view, field_path):
        super().__init__(field, request, params, model, admin_view, field_path)
        self.lookup_choices = Category.objects.filter(owner=request.user).values_list('id', 'name')


manager.register(CategoryOwnerFilter, take_priority=True)


class PostAdmin(BaseOwnerAdmin):
    list_display = ('id', 'title', 'category', 'status', 'created_time', 'operator', 'owner')
    form_layout = (
        Fieldset('基础配置',
            Row('title', 'category'),
                'status',
                'tags'
            ),
        Fieldset('内容', (
                'descripition',
                'content',
            ),
        ),
        Fieldset('额外信息', ({
            'classes': ('collapse',),
            'fields': ('tag',)
        })),
    )

    list_display_links = []  # 配置那些字段为链接（点击可进入文章详情页面）
    list_filter = ['category']   # 页面过滤器  需要通过哪些字段过滤列表页
    # list_filter = [CategoryOwnerFilter]    # 页面过滤器  展示自己定义的  不展示别人定义的
    search_fields = ['title', 'category__name']   # 配置搜索字段
    actions_on_bottom = True    # 是否展示在页面底部
    actions_on_top = True       # 是否展示在顶部
    save_on_top = True          # 保存  编辑 编辑并新建

    form = PostAdminForm             # 将字段修改成testare组件类型

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'

    def operator(self, obj):
        #
        return format_html('<a href="{}">编辑</a>', reverse('xadmin:blog_post_change', args=(obj.id,)))

    operator.short_description = '操作'    # 指定表头的展示文案

    @property
    def media(self):   # 自定义静态文件   若果是项目有的可以直接写项目绝对路径
        media = super().media
        media.add_js(['https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js'])
        media.add_css({
            'all': ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css', ),
        })

        return media


class LogEbtryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message']


xadmin.site.register(Tag, TagAdmin, site=custom_site)
xadmin.site.register(Category, CategoryAdmin, site=custom_site)
xadmin.site.register(Post, PostAdmin, site=custom_site)
xadmin.site.register(LogEntry, LogEbtryAdmin, site=custom_site)
