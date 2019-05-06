from dal import autocomplete
from blog.models import Category, Tag
from django import forms


class CategoryAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # 判断用户是否登录  未登录的返回空的queryset
        if not self.request.user.is_authenticated():
             Category.objects.none()

        qs = Category.objects.filter(owner=self.request.user)

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs


class TagAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Tag.objects.none()
        qs = Tag.objects.filter(owner=self.request.user)
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs



