"""
WSGI： web服务器网关接口， 规定了web server如何与网关进行交互  webserver其实就是一个用来装web应用的容器，通过他启动应用，连接HTTP服务，
保证所有的server程序能够与web框架或者协议进行交互

"""""
# coding:'utf-8'
import socket


# 单线程版本的web socket

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
# 发送的内容
body = '''from the5fire 《Django企业开发实战》'''
# 响应参数
response_params = [
    '\r\n'
    'HTTP/1.0 200 OK',
    'Date: Sat, 10 jun 2017 01:01:01 GMT',
    'Content-Type: text/plain; charset=utf-8',
    'Content-Length: {length}\r\n',
    body,
]
# 书籍中 此处为b'' 经验证是不正确的  接收到响应 解析的时候在进行转换
response = '\r\n'.join(response_params)


def handle_connection_single(conn, addr):
    request = b''
    while EOL1 not in request and EOL2 not in request:
        # 接收对方发送过来的请求
        request += conn.recv(1024)

    # 给对方发送我们的响应信息
    conn.send(response.encode('utf-8'))
    conn.close()


def main_single():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)    # 端口复用
    server_socket.bind(('127.0.0.1', 8000))                                # 绑定端口号
    server_socket.listen(5)                                                # 设置监听  将主动套接字变为被动套接字
    print('http://127.0.0.1:8000')
    try:
        while True:
            # 等待传入连接。返回一个新的套接字
            # 表示连接和客户端的地址。
            # 对于IP套接字，地址信息是一对(hostaddr, port)。
            conn, address = server_socket.accept()
            # 客户端发送信息回来之后  才会继续往下面走
            handle_connection_single(conn, address)               # 用新的套接字进行连接  收发消息

    finally:
        server_socket.close()


if __name__ == '__main__':
    main_single()


