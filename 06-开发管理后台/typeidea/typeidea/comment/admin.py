from django.contrib import admin
from .models import Comment

from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin
# Register your models here.


class CommentAdmin(BaseOwnerAdmin):
    list_display = ('nickname', 'status', 'email', 'content', 'created_time')
    fields = ('nickname', 'status')


admin.site.register(Comment, CommentAdmin, site=custom_site)

