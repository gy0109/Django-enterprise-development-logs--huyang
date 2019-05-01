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
        try:
            tag = Tag.objects.get(id=tag_id)       # 多对多的情况下 实现关联取值
        except Tag.DoesNotExist:
            post_list = []
        else:
            post_list = tag.post_set.filter(status=Post.STATUS_NORMAL)

    else:
        post_list = Post.objects.filter(status=Post.STATUS_NORMAL)
        if category_id:
            try:
                category = Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                category = None
            else:
                post_list = post_list.filter(category_id=category_id)

    return HttpResponse(tem.render(locals()))


def post_detail(request, post_id=None):
    # 文章详情页面的 展示
    tem = get_template('detail.html')
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None
    return HttpResponse(tem.render(locals()))

