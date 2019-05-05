from django.conf.urls import url
from . import views

urlpatterns = [
    # 博客首页：  https://www.gy.com
    # 博文详情页： https://www.gy.com/post/<post_id>.html
    # 分类列表页： https://www.gy.com/category/<category_id>.html
    # 标签详情页： https://www.gy.com/tag/<tag.id>
    # 友链详情页：https://www.gy.com/links/

    # url(r'^$', views.post_list, name='index'),
    url(r'^$', views.PostListView.as_view(), name='index'),


    # url(r'post/(?P<post_id>\d+).html/$', views.post_detail, name='post-detail'),
    # 除了使用as_view()接收请求和返回响应  之外   pk 参数作为过滤post数据点额参数，产生post.objects.filter(pk=pk) 以拿到文章的实例
    url(r'post/(?P<pk>\d+).html/$', views.PostDetailView.as_view(), name='post-detail'),

    url(r'category/(?P<pk>\d+)/$', views.PostListView.as_view(), name='category-list'),
    url(r'tag/(?P<pk>\d+)/$', views.PostListView.as_view(), name='tag-list'),
]

