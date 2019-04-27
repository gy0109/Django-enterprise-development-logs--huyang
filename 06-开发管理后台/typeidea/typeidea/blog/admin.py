from django.contrib import admin
from .models import Tag, Category, Post

# Register your models here.


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_nav', 'created_time')
    fields = ('name', 'status', 'is_nav')


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'owner', 'created_time')
    fields = ('title', 'status', 'owner')


admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)