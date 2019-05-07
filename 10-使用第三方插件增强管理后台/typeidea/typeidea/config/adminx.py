import xadmin
from .models import SiderBar, Link
from typeidea.base_admin import BaseOwnerAdmin


class SiderBarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'display_type', 'status', 'created_time', 'content', 'owner')
    fields = ('title', 'status', 'content', 'display_type')


class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title', 'href', 'status', 'created_time')
    fields = ('title', 'href', 'status')


xadmin.site.register(SiderBar, SiderBarAdmin)
xadmin.site.register(Link, LinkAdmin)
