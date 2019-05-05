from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template

# Create your views here.
from django.views.generic import DetailView, ListView
from django.views.generic.base import View

from .models import Post, Tag, Category
from config.models import SiderBar


# def post_list(request, category_id=None, tag_id=None):
#     # 标签页和分类页
#     # tem = get_template('list.html')
#     tag = None
#     category = None
#
#     if tag_id:
#        post_list , tag = Post.get_by_tag(tag_id)
#
#     elif category_id:
#         post_list, category = Post.get_by_category(category_id)
#     else:
#         post_list = Post.latest_posts()
#
#     context = {
#         'post_list': post_list,
#         'category': category,
#         'tag': tag,
#         'sidebars': SiderBar.get_all(),
#     }
#     #
#     context.update(Category.get_navs())
#     return render(request, 'blog/list.html', context=context)
#     # return HttpResponse(tem.render(locals()))


"""
django提供的cbv：
ListView：继承view实现了get 方法 通过绑定模板批量获取数据
DetailView: 继承view实现了get 方法 通过绑定模板  获取单个实例数据
View: 给予HTTP的分发逻辑， 调用对应的方法
TemplateView:直接用来返回指定的模板，传递变量到模板中来进行数据展示

开闭原则

as_view函数接收请求和反回响应，
"""
#
#
# class PostListView(ListView):
#     首页
#     queryset = Post.latest_posts()   # 只针对于文章的显示
#     paginate_by = 1  # 分页
#     # model = Post
#     context_object_name = 'post_list'
#     template_name = 'blog/list.html'

"""
queryset : 和model类似 二选一， 设定基础的数据集， model的设定没有过滤的功能，可以通过queryset= 进行过过滤
paginate_by          # 分页
model :   指定当前view要使用的模板
context_object_name ： 设置模板中使用的字段名称
template_name = 'blog/list.html'  指定模板名
get_queryset： 用来获取数据   若指定了queryset自己返回queryset需要的数据
get_object： 根据url参数 从queryset获取相应的实例
get_context_data: 获取渲染到模板的上下文，如果有新增数据的需要传递到模板，可以重写该方法


"""
# def post_detail(request, post_id=None):
#     # 文章详情页面的 展示
#     # tem = get_template('detail.html')
#     try:
#         post = Post.objects.get(id=post_id)
#     except Post.DoesNotExist:
#         post = None
#
#     context = {
#         'post': post,
#         'sidebars': SiderBar.get_all(),
#     }
#     context.update(Category.get_navs())
#     # return HttpResponse(tem.render(locals().update(Category.get_navs())))
#     return render(request, 'detail.html', context=context)


class CommonViewMixin:
    # 处理通用数据
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'sidebars': SiderBar.get_all(),
        })
        context.update(Category.get_navs())
        context.update(Tag.get_tag())
        return context


class PostDetailView(CommonViewMixin, DetailView):
    # 文章详情页面的 展示
    queryset = Post.latest_posts()
    template_name = 'blog/detail.html'    # 渲染数据
    context_object_name = 'post'
    # pk_url_kwarg = 'post_id'       # 代替pk键的键名 可以不设置  url中依然使用pk


class IndexView(CommonViewMixin, ListView):
    # 首页
    queryset = Post.latest_posts()
    paginate_by = 2
    center_object_name = 'post_list'
    template_name = 'blog/list.html'


# 分类详情页和标签详情页
# queryset 的数据徐亚根据当前的分类或者标签进行分类过滤
# 渲染到模板上的数据需要加上当前选择分类的数据

class CategoryView(IndexView):
    # 分类页
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')   # category_id 数据其实是从url中拿到的
        category = get_object_or_404(Category, pk=category_id)  # get_object_or_404 快捷方式 获取一个对象的额实例 获取到就返回实例 获取不到就返回404
        context.update({
            'category': category
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id)


class TagView(IndexView):
    # 标签页
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag')
        tag = get_object_or_404(Tag, pk=tag_id)
        context.update({
            'tag': tag
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        tag_id = self.kwargs.get('tag')
        return queryset.filter(tag=tag_id)



