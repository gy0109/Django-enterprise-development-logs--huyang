

# 创建admin基类   方便所有的 app.admin 使用
class BaseOwnerAdmin:
    exclude = ('owner', )

    def save_model(self):
        self.new_obj.owner = self.request.user
        return super().save_model()

    def get_list_queryset(self):  # 展示自己的标签
        request = self.request
        qs = super().get_list_queryset()
        return qs.filter(owner=request.user)
