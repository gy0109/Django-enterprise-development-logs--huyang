import xadmin

from .models import Comment


# 无需继承  不需要owner字段  并且评论作者自己不可以修改或者增加之类的
class CommentAdmin:
    list_display = ('nickname', 'status', 'email', 'content', 'created_time')
    model_icon = 'fa fa-comment-o'


xadmin.site.register(Comment, CommentAdmin)

