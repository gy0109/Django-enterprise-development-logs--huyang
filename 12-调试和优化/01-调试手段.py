# 1. print大法
# 2. logging大法
# 3. pdb大法


# 2. logging
"""
version: 固定值为1
formatter: 格式化设置的输出内容
handlers： 处理打印日志内容， 设定是输出到文件还是输出到stream 以及使用哪一种formatter
loggers: 定义不同的名称 级别，和有哪些handle，  第一个key为‘’的是默认的
"""

"""
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
            'standard': {
                'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
            },
        },
    'filters': {
        },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'default': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(STATIC_ROOT+'/logs/','all.log'), #或者直接写路径：'c:\logs\all.log',
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'request_handler': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(STATIC_ROOT+'/logs/','script.log'), #或者直接写路径：'filename':'c:\logs\request.log''
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },
        'scprits_handler': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(STATIC_ROOT+'/logs/','script.log'), #或者直接写路径：'filename':'c:\logs\script.log'
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
            },
        },
    'loggers': {
        '': {
            'handlers': ['comsole'],
            'level': logging.DEBUG
        },
        'django': {
            'handlers': ['default','console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'XieYin.app':{
            'handlers': ['default','console'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': False
        },
        'scripts': { # 脚本专用日志
            'handlers': ['scprits_handler'],
            'level': 'INFO',
            'propagate': False
        },
    }
}
"""

# 3. pdb大法  追踪代码流程
# pdb 提供了REPL（交互式执行环境）
import pdb

pdb.set_trace()   # 进入pdb交互式模式  可以向Python shell一样获取所有的变量和值

# 最简单的使用方法  是直接使用 pdb执行文件
# python -m pdb hello.py


# 还可以下断点 import pdb; pdb.set_trace()  断点带入  会让我们看到接下来的 执行过程

"""
s: step in 用来跳入某个执行过程中
n: next 下一句
c: continue  恢复执行状态
l: list 列出当前要执行的语句的上下文 l会记录状态  每次输入l都是从上一次停止的地方进入的
ll: long list  展示当前函数的额所有代码，每次执行结果都一样
r: return 太长的执行过程中  用来跳出
q: quit 退出
exit: 退出

"""