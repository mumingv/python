# -*- coding: UTF-8 -*-
'''
/***********************************************************
      FileName: listing14-4.py
          Desc: 源生ForkingTCPServer
        Author: Jie Yin
         Email: mumingv@163.com
      HomePage: https://github.com/mumingv
       Version: 0.0.1
    LastChange: 2017-05-30 12:27:03
       History:
 ***********************************************************/
'''
from SocketServer import ForkingTCPServer, StreamRequestHandler
import time

class Handler(StreamRequestHandler):

    def handle(self):
        addr = self.request.getpeername()
        print 'Got connection from', addr
        # 延迟5秒
        time.sleep(5)
        self.wfile.write('Thank you for connecting')
        print 'Send data to', addr, 'ok'

# Server是一个ForkingTCPServer，所以对于每个客户端请求都会自动创建一个Handler实例
# ForkingTCPServer是异步的，对于每个请求，服务端都会fork一个子进程来处理客户端请求，所以同时会有多个Handler实例在跑
server = ForkingTCPServer(('', 1234), Handler)
server.serve_forever()
