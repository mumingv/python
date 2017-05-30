# -*- coding: UTF-8 -*-
'''
/***********************************************************
      FileName: listing14-5.ThreadingTCPServer2.py
          Desc: 原生ThreadingTCPServer
        Author: Jie Yin
         Email: mumingv@163.com
      HomePage: https://github.com/mumingv
       Version: 0.0.1
    LastChange: 2017-05-30 12:54:54
       History:
 ***********************************************************/
'''
from SocketServer import ThreadingTCPServer, StreamRequestHandler
import time

class Handler(StreamRequestHandler):

    def handle(self):
        addr = self.request.getpeername()
        print 'Got connection from', addr
        time.sleep(5)
        self.wfile.write('Thank you for connecting ThreadingTCPServer(origin)')
        print 'Send data to', addr, 'ok'

server = ThreadingTCPServer(('', 1234), Handler)
server.serve_forever()
