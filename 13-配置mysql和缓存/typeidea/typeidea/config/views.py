from django.views.generic import ListView
from blog.views import CommonViewMixin
from .models import Link
# Create your views here.


class LinksListView(CommonViewMixin, ListView):
    queryset = Link.objects.filter(status=Link.STATUS_NORMAL)  # 取出一个列表
    template_name = 'config/links.html'  # 模板名称
    context_object_name = 'link_list'   # 在模板中使用link_list作为参数传递





