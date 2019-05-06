from django.conf.urls import url
from django.contrib.sitemaps import views as sitemap_views
from blog.rss import LatestPostFeed
from blog.sitemap import PostSitemap
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


    url(r'^search/$', views.SearchView.as_view(), name='search'),
    url(r'^author/(?P<owner_id>\d+)/$', views.AuthorView.as_view(), name='author'),

    # RSS和sitemap的url
    url(r'^rss|feed/', LatestPostFeed(), name='rss'),
    url(r'^sitemap\.xml$', sitemap_views.sitemap, {'sitemaps': {'posts': PostSitemap()}}),
]

