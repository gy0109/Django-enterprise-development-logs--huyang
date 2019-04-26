# coding: utf-8


def simple_app(environ, start_response):
    status = '200 OK'
    response_header = ['Content-Type', ' text/plain']
    start_response(status, response_header)
    return [b'hello world, this is gy']


class AppClass(object):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]

    def __call__(self, environ, start_response):
        start_response(self.status, self.response_headers)
        return [b'Hello word ']


#  application必须是一个可调用对象
application = AppClass()


def simple_app_package(environ, start_response):
    response = start_response("200 OK", [("Content-type", "text/html;charset= utf-8")])
    return response

