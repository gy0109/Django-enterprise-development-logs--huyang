# 前台负责展示现有学员   后台处理申请

# 创建虚拟环境 ： mkvirtualenv staudent-env -p 'which python3.6'
# 激活虚拟环境 : workon staudent-env
# 下载django  pip install

# 1. 开发首页

# 2. 输出数据

# 3.提交数据Form表单

# 4. 优化数据逻辑
# students = Student.get_all()           # 配合model中的get_all模块可以将获取数据逻辑封装到model层
# @classmethod
#     def get_all(cls):
#         return cls.objects.all()


# 5. HttpResponseRedirect(reverse('index'))    url(, name='')    不然报错


# 6. 在choices字段中  指定get_status_display  无参数的方法进行调用  不写（）
#

# 7， """"
# 中间件： init 确定是否启用当前中间键
#         process_request     请求之前    用户登录校验和Http请求头校验
#         process_view    响应之前        func为我们要执行的视图函数名如果返回NoneDjango会自动执行其他view函数
#         process_exception    异常处理   只用触发异常才会被执行
#         process_template_response  模板响应之前    content-type  headers等设置
#         process_response        处理视图函数之前          返回None或者HTTPResponse对象
#
#
#         中间键的读取顺序是  自上而下的    执行顺序是从下往上的
# """

# 8， 数据库 的单元测试   Django自动帮助创建的基于内存的测试数据库
# 'TEST': {
#     'NAME': 'mytextdatabase',  # 配置单元测试的的数据库
# }



