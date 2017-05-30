# -*- coding: UTF-8 -*-
'''
/***********************************************************
      FileName: client.py
          Desc: 异步IO: select示例
        Author: Jie Yin
         Email: mumingv@163.com
      HomePage: https://github.com/mumingv
       Version: 0.0.1
    LastChange: 2017-05-30 14:51:30
       History:
 ***********************************************************/
'''
# 源码参考：http://www.cnblogs.com/coser/archive/2012/01/06/2315216.html

import socket
import time
 
messages = ["This is the message",
            "It will be sent",
            "in parts"]
 
print "Connect to the server"
 
server_address = ("", 10001)
 
# 创建套接字数组
socks = []
for i in range(10):
    socks.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
 
# 连接到服务器
for s in socks:
    s.connect(server_address)
 
counter = 0
for message in messages :
    # 发送数据
    for s in socks:
        counter += 1
        print "  %s sending %s" % (s.getpeername(), (message + " version " + str(counter)))
        s.send(message + " version " + str(counter))
    # 接收数据
    for s in socks:
        data = s.recv(1024)
        print " %s received %s" % (s.getpeername(), data)
        if not data:
            print "closing socket ", s.getpeername()
            s.close()

#time.sleep(10)
