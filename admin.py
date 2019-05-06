from django.contrib import admin
from .models import Comment

from typeidea.custom_site import custom_site
# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'status', 'email', 'content', 'created_time')
    fields = ('nickname', 'status')


admin.site.register(Comment, site=custom_site)

