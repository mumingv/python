# -*- coding: UTF-8 -*-
'''
/***********************************************************
      FileName: listing14-6.async.io.select.py
          Desc: 异步IO: select
        Author: Jie Yin
         Email: mumingv@163.com
      HomePage: https://github.com/mumingv
       Version: 0.0.1
    LastChange: 2017-05-30 13:06:16
       History:
 ***********************************************************/
'''
import socket, select

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)
inputs = [s]
while True:
    # select如果没有第4个参数(超时)会阻塞，如果有第4个参数(超时)会超时返回空列表
    #rs, ws, es = select.select(inputs, [], [])
    rs, ws, es = select.select(inputs, [], [], 2)
    print '123'
    for r in rs:
        print '456---'
        if r is s:
            c, addr = s.accept()
            print 'Got connection from', addr
            inputs.append(c)
        else:
            try:
                data = r.recv(1024)
                disconnected = not data
            except socket.error:
                disconnected = True

            if disconnected:
                print r.getpeername(), 'disconnected'
                inputs.remove(r)
            else:
                print data
