# -*- coding: UTF-8 -*-
'''
/***********************************************************
      FileName: listing14-5.ThreadingTCPServer.py
          Desc: 自定义ThreadingTCPServer
        Author: Jie Yin
         Email: mumingv@163.com
      HomePage: https://github.com/mumingv
       Version: 0.0.1
    LastChange: 2017-05-30 12:55:00
       History:
 ***********************************************************/
'''
from SocketServer import TCPServer, ThreadingMixIn, StreamRequestHandler
import time

class Server(ThreadingMixIn, TCPServer): pass

class Handler(StreamRequestHandler):

    def handle(self):
        addr = self.request.getpeername()
        print 'Got connection from', addr
        time.sleep(5)
        self.wfile.write('Thank you for connecting ThreadingTCPServer')
        print 'Send data to', addr, 'ok'

server = Server(('', 1234), Handler)
server.serve_forever()
