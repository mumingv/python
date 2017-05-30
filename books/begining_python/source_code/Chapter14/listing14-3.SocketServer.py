# -*- coding: UTF-8 -*-
'''
/***********************************************************
      FileName: listing14-3.py
          Desc: SocketServer代替基本的socket server
        Author: Jie Yin
         Email: mumingv@163.com
      HomePage: https://github.com/mumingv
       Version: 0.0.1
    LastChange: 2017-05-29 23:25:07
       History:
 ***********************************************************/
'''

# 基于BaseServer类的派生类
'''
+------------+
| BaseServer |
+------------+
      |
      v
+-----------+        +------------------+
| TCPServer |------->| UnixStreamServer |
+-----------+        +------------------+
      |
      v
+-----------+        +--------------------+
| UDPServer |------->| UnixDatagramServer |
+-----------+        +--------------------+
'''

# 基于BaseRequestHandler类的派生类
'''
                 +--------------------+
           +-----| BaseRequestHandler |-----+
           |     +--------------------+     |
           |                                |
           v                                v
+----------------------+        +------------------------+
| StreamRequestHandler |        | DatagramRequestHandler |
+----------------------+        +------------------------+
'''

# 流程步骤
'''
1. 根据需要选择一个合适的服务类型，如，面向TCP连接的多进程服务器：ForkingTCPServer；
2. 创建一个请求处理器（request handler）类型，这个类型的 handle()（类似于回调函数）方法中定义如何处理到达的客户端连接。
3. 实例化服务器，传入服务器绑定的地址和第2步定义的请求处理器类；
4. 调用服务器实例的 handle_request() 或 serve_forever() 方法，一次或多次处理客户请求。
'''

from SocketServer import TCPServer, StreamRequestHandler

# 自定义一个请求处理类，其基于StreamRequestHandler类派生而来
class Handler(StreamRequestHandler):

    # 重写基类中的handle方法，用于处理客户端请求
    def handle(self):
        # self.request等同于socket.accept返回的新建的socket(用于连接客户端)
        addr = self.request.getpeername()
        print 'Got connection from', addr
        self.wfile.write('Thank you for connecting')

# 实例化一个TCPServer：第一个参数为server_address, (IP, PORT)中IP为空时表示本机；第二个参数为用户自定义的请求处理类，当每处理一个客户端请求时都会自动创建一个请求处理类的实例
server = TCPServer(('', 1234), Handler)

# 启动服务器并循环处理客户请求
server.serve_forever()
