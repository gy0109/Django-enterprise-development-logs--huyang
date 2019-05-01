from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

# Create your views here.
from .models import Post, Tag, Category


def post_list(request, category_id=None, tag_id=None):
    # 标签页和分类页
    tem = get_template('list.html')
    tag = None
    category = None

    if tag_id:
       post_list , tag = Post.get_by_tag(tag_id)

    elif category_id:
        post_list, category = Post.get_by_category(category_id)
    else:
        post_list = Post.latest_posts()

    return HttpResponse(tem.render(locals()))


def post_detail(request, post_id=None):
    # 文章详情页面的 展示
    tem = get_template('detail.html')
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None
    return HttpResponse(tem.render(locals()))

