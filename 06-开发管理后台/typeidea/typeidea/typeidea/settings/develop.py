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


