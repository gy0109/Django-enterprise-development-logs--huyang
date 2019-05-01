






# 3. SimpleListFilter是admin实现自定义过滤器 两个方法和两个属性
# title : 标题  parameter_name 是查询时url参数名字
# lookups： 返回要展示的内容和要查询的id
# queryset: 根据url query 的内容返回列表页数据，

# 4. get_queryset() 实现自己的分类标签和文章


5. # Form 是对用户输入以及model中要展示的数据的抽象
    # model是展示的数据


# @admin.register(Category, site=custom_site)
# class CategoryAdmin(BaseOwnerAdmin):
#     def post_count(self, obj):
#         return obj.post_set.count()
#
#     post_count.short_description = '文章数量'
#
#
#
#
# @admin.register(LogEntry, site=custom_site)
# class LogEntryAdmin(admin.ModelAdmin):
#     list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message']
