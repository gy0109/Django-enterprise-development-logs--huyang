from django.conf.urls import url
from . import views

urlpatterns = [
    # 博客首页：  https://www.gy.com
    # 博文详情页： https://www.gy.com/post/<post_id>.html
    # 分类列表页： https://www.gy.com/category/<category_id>.html
    # 标签详情页： https://www.gy.com/tag/<tag.id>
    # 友链详情页：https://www.gy.com/links/

    url(r'^$', views.post_list),
    url(r'post/(?P<post_id>\d+).html$', views.post_detail),
    url(r'category/(?P<category_id>\d+)/$', views.post_list),
    url(r'tag/(?P<tag_id>\d+)/$', views.post_list),
]


