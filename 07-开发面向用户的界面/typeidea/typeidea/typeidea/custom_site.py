from django.contrib.admin import AdminSite


# url.py     admin.site.urls
# admin.site.register

# 一般情况下只需要一个site就可以了，   一个site对应一个站点，


class CustomSite(AdminSite):
    site_header = 'TYPEIDEA'
    site_title = 'Typeidea管理后台'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')
