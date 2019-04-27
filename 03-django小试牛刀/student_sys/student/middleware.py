import time
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

"""
中间件： init 确定是否启用当前中间键
        process_request     请求之前    用户登录校验和Http请求头校验
        process_view    响应之前        func为我们要执行的视图函数名如果返回NoneDjango会自动执行其他view函数
        process_exception    异常处理   只用触发异常才会被执行
        process_template_response  模板响应之前    content-type  headers等设置
        process_response        处理视图函数之前          返回None或者HTTPResponse对象
        
        
        中间键的读取顺序是  自上而下的    执行顺序是从下网上的 
"""


class TimeMiddleware(MiddlewareMixin):
    def process_request(self, reqeust):
        self.start_time = time.time()
        return

    def process_view(self, reqeust, func, *args, **kwargs):
        if reqeust.path != reverse('index'):
            return None

        start = time.time()
        response = func(reqeust)
        costed = time.time() - start
        print('process view : {:.2fs}'.format(costed))
        return response

    def process_exception(self, reqeust): pass   # 只用发生异常才会调用

    def process_template_response(self, reqeust, response): return response

    def process_response(self, reqeust, response):
        costed = time.time() - self.start_time
        print('request to response cose: {:.2fs}'.format(costed))
        return response



