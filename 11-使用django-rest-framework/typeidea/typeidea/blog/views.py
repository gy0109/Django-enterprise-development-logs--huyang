from datetime import date
from django.core.cache import cache
from django.db.models import Q, F
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Post, Tag, Category
from config.models import SiderBar


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

    def get(self, reqeust, *args, **kwargs):
        # pv uv最新最热文章
        response = super().get(reqeust, *args, **kwargs)
        self.handle_visited()
        return response

    def handle_visited(self):
        increade_pv = False
        increade_uv = False
        uid = self.request.uid
        pv_key = 'pv: %s:%s' % (uid, self.request.path)
        uv_key = 'uv: %s:%s:%s' % (uid, str(date.today()), self.request.path)
        if not cache.get(pv_key):    # 从缓存中找到pv  uv
            increade_pv = True
            cache.set(pv_key, 1, 1*60)

        if not cache.get(uv_key):
            increade_uv = True
            cache.set(uv_key, 1, 24*60*60)

        # 根据逻辑进行增加
        if increade_pv and increade_uv:
            Post.objects.filter(pk=self.object.id).update(pv=F('pv')+1, uv=F('uv')+1)
        elif increade_uv:
            Post.objects.filter(pk=self.object.id).update(uv=F('uv') + 1)
        elif increade_pv:
            Post.objects.filter(pk=self.object.id).update(pv=F('pv') + 1)


class IndexView(CommonViewMixin, ListView):
    # 首页
    queryset = Post.latest_posts()
    paginate_by = 2
    center_object_name = 'post_list'
    template_name = 'blog/list.html'


class CategoryView(IndexView):
    # 分类页
    def get_context_data(self, **kwargs):
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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        tag = get_object_or_404(Tag, pk=tag_id)
        context.update({
            'tag': tag
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        tag_id = self.kwargs.get('tag_id')
        return queryset.filter(tag__id=tag_id)


class SearchView(IndexView):
    # 搜索功能
    def get_context_data(self):
        context = super().get_context_data()
        context.update({
            'keyword': self.request.GET.get('keyword', '')
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.GET.get('keyword')
        if not keyword:
            return queryset
        # 返回title中或者description中包含keyword的内容
        return queryset.filter(Q(title__icontains=keyword) | Q(descripition__icontains=keyword))


class AuthorView(IndexView):
    # 作者过滤
    def get_queryset(self):
        queryset = super().get_queryset()
        author_id = self.kwargs.get('owner_id')
        return queryset.filter(owner_id=author_id)

