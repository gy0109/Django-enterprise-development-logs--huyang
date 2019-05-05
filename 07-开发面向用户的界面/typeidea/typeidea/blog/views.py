from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

# Create your views here.
from django.views.generic import DetailView, ListView

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


class PostListView(ListView):
    queryset = Post.latest_posts()
    # paginate_by = 1           # 分页
    # model = Post
    context_object_name = 'post_list'
    template_name = 'blog/list.html'


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


class PostDetailView(DetailView):
    # 文章详情页面的 展示
    model = Post
    template_name = 'blog/detail.html'    # 渲染数据

