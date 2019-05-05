from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

# Create your views here.
from django.views.generic import DetailView, ListView

from .models import Post, Tag, Category
from config.models import SiderBar


def post_list(request, category_id=None, tag_id=None):
    # 标签页和分类页
    # tem = get_template('list.html')
    tag = None
    category = None

    if tag_id:
       post_list , tag = Post.get_by_tag(tag_id)

    elif category_id:
        post_list, category = Post.get_by_category(category_id)
    else:
        post_list = Post.latest_posts()

    context = {
        'post_list': post_list,
        'category': category,
        'tag': tag,
        'sidebars': SiderBar.get_all(),
    }
    #
    context.update(Category.get_navs())
    return render(request, 'blog/list.html', context=context)
    # return HttpResponse(tem.render(locals()))


class PostList(ListView):
    queryset = Post.latest_posts()
    paginate_by = 1
    model = Post
    context_object_name = 'post_list'
    template_name = 'blog/list.html'

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

class PostDetail(DetailView):
    # 文章详情页面的 展示
    model = Post
    template_name = 'blog/detail.html'

