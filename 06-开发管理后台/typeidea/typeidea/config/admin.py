from django.contrib import admin
from .models import SiderBar, Link

from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin
# Register your models here.


class SiderBarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'display_type', 'status', 'created_time')
    fields = ('title', 'status')


class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title', 'href', 'status', 'created_time')
    fields = ('title', 'status')


admin.site.register(SiderBar, SiderBarAdmin, site=custom_site)
admin.site.register(Link, LinkAdmin, site=custom_site)
