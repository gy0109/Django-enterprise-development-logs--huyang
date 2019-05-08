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
       # 'CONN_MAX_AGE': 5*60,   # 最大连接数  默认100  多线程和gevent 等不建议配置  复用性
       # gevent会给Python的线程打补丁  导致数据库的复用性降低
       # 'OPTIONS': {'charset': 'utf8m64'}   # 字符编码级  m64支持emjio表情
       # CREATE DATABASE TYPEIDEA CHARACTER SET UTF8M64 CILLATE utf8m64_unicode_ci;
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
