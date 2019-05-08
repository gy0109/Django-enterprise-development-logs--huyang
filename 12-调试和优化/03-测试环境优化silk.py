
# 配置silk
# 1. pip install django-silk==3.0.0
# 2. INSTALLeD_APPS += ['silk',]
#     MIDDLEWARE += ['silk.middleware.SilkMiddleware',]
# 3.if setting.DEBUG:
# 	urlpatterns += [url(r'^silk/', include('silk.urls', namespace='silk'))]
# 4.建表 ./manage.py migrate
# 5. 访问几个页面后打开silk页面 可以看到三个页面  detail,浏览器network可以看到的数据 sql可以看到具体SQL请求的是由哪一句发起的 profiling需要配置


# 配置profiling
# from silk.profiling.profiler import silk_profile
#
# class CommonsMixin(object):
#     @silk_profile(name='get_navs')
#     def get_navs(self):
#         pass
#
# 类似如此的view函数中进行添加
