from django.conf.urls import url
from . import views

urlpatterns = [
    # 博客首页：  https://www.gy.com
    # 博文详情页： https://www.gy.com/post/<post_id>.html
    # 分类列表页： https://www.gy.com/category/<category_id>.html
    # 标签详情页： https://www.gy.com/tag/<tag.id>
    # 友链详情页：https://www.gy.com/links/

    # url(r'^$', views.post_list, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),   # 首页

    # 文章详情页
    # url(r'post/(?P<post_id>\d+).html/$', views.post_detail, name='post-detail'),
    # 除了使用as_view()接收请求和返回响应  之外   pk 参数作为过滤post数据点额参数，产生post.objects.filter(pk=pk) 以拿到文章的实例
    url(r'post/(?P<pk>\d+).html/$', views.PostDetailView.as_view(), name='post-detail'),

    # 标签页和分类页
    url(r'category/(?P<category_id>\d+)/$', views.CategoryView.as_view(), name='category-list'),
    url(r'tag/(?P<tag_id>\d+)/$', views.TagView.as_view(), name='tag-list'),

    """
    as_view函数的处理过程：只
    
    做了一件事 返回了一个闭包  Django解析完成后调用
    给view赋值， reqeust, args, kwargs
    根据http方法分发请求， 
    
    请求完成后的逻辑：
    1， 请求到达之后，会首先调用get_queryset方法，拿到数据源
    2.  接着会调用get_context_data方法，拿到需要渲染的数据源
     1， get_context_Data 首先调用get_paginate_by 拿到分页数据
     2. 接着调用get_context_object_name 拿到渲染模板的queryset的名称，
     3.调用paginate_queryset进行分页处理请求
     4.拿到数据转为dictionary 并返回
    
    3. 调用render_to_response渲染到页面
        1. 在render_to_response中调用get_template_names拿到模板名
        2. 吧request, context, template_name 传递到模板中
    """
]

