# -*- coding: UTF-8 -*-
'''
/***********************************************************
      FileName: listing14-4.py
          Desc: 
        Author: Jie Yin
         Email: mumingv@163.com
      HomePage: https://github.com/mumingv
       Version: 0.0.1
    LastChange: 2017-05-30 12:27:03
       History:
 ***********************************************************/
'''
from SocketServer import TCPServer, ForkingMixIn, StreamRequestHandler
import time

# 该类等同于SocketServer库自带的ForkingTCPServer
# ！注意：多重继承时，ForkingMixIn需要放在TCPServer前面
class Server(ForkingMixIn, TCPServer): pass

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
server = Server(('', 1234), Handler)
server.serve_forever()
