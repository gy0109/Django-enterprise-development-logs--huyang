import xadmin
from django.contrib import admin

from .models import Comment
from typeidea.base_admin import BaseOwnerAdmin
# Register your models here.


# 无需继承  不需要owner字段  并且评论作者自己不可以修改或者增加之类的
class CommentAdmin:
    list_display = ('nickname', 'status', 'email', 'content', 'created_time')


xadmin.site.register(Comment, CommentAdmin)

