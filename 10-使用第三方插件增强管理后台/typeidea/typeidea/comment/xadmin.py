import xadmin
from .models import Comment
from typeidea.base_admin import BaseOwnerAdmin
from typeidea.custom_site import custom_site
# Register your models here.


class CommentAdmin(BaseOwnerAdmin):
    list_display = ('nickname', 'status', 'email', 'content', 'created_time')
    fields = ('nickname', 'status')


xadmin.site.register(Comment, site=custom_site)

