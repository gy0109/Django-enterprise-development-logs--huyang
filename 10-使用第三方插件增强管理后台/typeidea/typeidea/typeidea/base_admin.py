

# 创建admin基类   方便所有的 app.admin 使用
class BaseOwnerAdmin:
    exclude = ('owner', )   # 编辑页面隐藏字段
    # xadmin配置
    enable_themes = True
    use_bootswatch = True
    site_title = "Typeidea运营管理系统"  # 设置站点标题
    site_footer = "Typeidea@gy"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠
    list_export = ['xls', 'csv', 'xml']  # 导出的数据格式
    refresh_times = [3, 5]  # 可选以支持按多长时间(秒)刷新页面

    def get_list_queryset(self):  # 展示自己的标签
        request = self.request
        qs = super().get_list_queryset()
        return qs.filter(owner=request.user)

    def save_models(self):
        self.new_obj.owner = self.request.user
        return super().save_models()

