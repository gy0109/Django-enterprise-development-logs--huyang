from .base import *

DEBUG = True

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.mysql',
       'NAME': 'typeidea',
       'USER': 'root',
       'PASSWORD': 'gy0109',
       'HOST': '127.0.0.1',
       'PORT': '3306',

       'TEST': {
           'CHARSET': 'utf8',            #
           # 'COLLATION': 'utf8_general_ci',
           'NAME': 'mytextdatabase',      # 配置单元测试的的数据库
       },
       # 'CHARSET': 'utf8'
    }
}

# debug_toolbar本地系统优化方式的配置
INSTALLED_APPS += [
    'debug_toolbar',
    'debug_toolbar_line_profiler',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']

# # debug_toobar本地系统优化配置--第三方包panel --火焰图
DEBUG_TOOLBAR_PANELS = [
    # 'djdt_flamegraph.FlamegraphPanel',   报错啊
    'debug_toolbar_line_profiler.panel.ProfilingPanel',

]

#