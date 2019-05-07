from django.conf.urls import url, include
from django.contrib.sitemaps import views as sitemap_views
from blog.rss import LatestPostFeed
from blog.sitemap import PostSitemap
from rest_framework.documentation import include_docs_urls

from . import views
from .autocomplete import CategoryAutoComplete, TagAutoComplete
from . import apis
from rest_framework.routers import DefaultRouter

# base_name可以代替namespace进行reverse操作
router = DefaultRouter()
router.register(r'post', apis.PostViewSet, base_name='api-post')

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

    # 搜索框自动补全
    url(r'^categoryautocomplete/$', CategoryAutoComplete.as_view(), name='categoryautocomplete'),
    url(r'^tagautocomplete/$', TagAutoComplete.as_view(), name='tagautocomplete'),


    # restframework的urls

    # api/post/ 页面化输出
    #  api/post/?format=json将数据一json格式输出
    # url(r'^api/post/$', apis.PostList.as_view(), name='post_list'),
    # docs工具的接口  -----------------rest-framework测试 需要安装依赖包 pip install coreapi==2.3.3
    url(r'^api/docs/', include_docs_urls(title='typeidea apis')),

    url(r'^api/', include(router.urls, ))  # namespace='api'rest_framework中有的地方并不支持recversehe recverse_acthion  所以使用router


    ]

