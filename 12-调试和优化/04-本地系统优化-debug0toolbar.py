# 1. 配置  debug为True  并且 是开发和测试环境下使用  故配置在develop.py文件内
pip install django_debug_toolbar

INSTALLED_APPS += ['debug_toolbar']

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']


# urls.py   debug模式下才能加载debug_toolbar模块。 启动项目  即可看到
if setting.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]+urlpatterns


2.  debug_toobar本地系统优化配置--第三方包panel --火焰图
pip  install djdt_flamegraph==0.2.12

DEBUG_TOOLBAR_PANELS = [
    'djdt_flamegraph.FlasmegraphPanel',
]

可以尝试加入time.sleep进行演示观察


# 3，line_profiler 行级性能分析
pip  install django-debug-toolbar-line-profiler
DEBUG_TOOLBAR_PANELS = [
    # 'djdt_flamegraph.FlamegraphPanel',   报错啊
    'debug_toolbar_line_profiler.panel.ProfilingPanel',
]

line: 行号
hits: 代码被执行的次数
Time：当前行执行的时间，除以定时器单元，
per hit 每次行执行消耗的时间
% Time执行时间占总时间的的比值
Line Contents 对应的代码