import xadmin
from .models import SiderBar, Link

from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin
# Register your models here.


class SiderBarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'display_type', 'status', 'created_time', 'content', 'owner')
    fields = ('title', 'status', 'content', 'display_type')


class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title', 'href', 'status', 'created_time')
    fields = ('title', 'href', 'status')


xadmin.site.register(SiderBar, SiderBarAdmin, site=custom_site)
xadmin.site.register(Link, LinkAdmin, site=custom_site)
