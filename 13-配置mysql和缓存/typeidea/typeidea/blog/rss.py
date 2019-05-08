from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils.feedgenerator import Rss201rev2Feed
from .models import Post


# 定制输出正文部分的了类型
class ExtendedRSSFeed(Rss201rev2Feed):
    def add_item_elements(self, handler, item):
        super(ExtendedRSSFeed, self).add_item_elements(handler, item)
        handler.addQuickElement('content:html', item('content_html'))


class LatestPostFeed(Feed):
    feed_type = ExtendedRSSFeed       # 默认为Rss201rev2Feed  但是可以定制
    title = 'Typeidea Blog Systerm'
    links = '/rss/'
    description = 'typeidea is a blog system power by django'

    def items(self):
        return Post.objects.filter(statua=Post.STATUS_NORMAL)[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_extra_kwargs(self, item):
        return {'content_html': self.item_content_html(item)}

    def item_content_html(self, item):
        return item.content_item

    def item_link(self, item):
        return reverse('post-detail', args=[item.pk])
