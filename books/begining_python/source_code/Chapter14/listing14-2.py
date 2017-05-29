# -*- coding: UTF-8 -*-
'''
/***********************************************************
      FileName: listing14-2.py
          Desc: socket客户端
        Author: Jie Yin
         Email: mumingv@163.com
      HomePage: https://github.com/mumingv
       Version: 0.0.1
    LastChange: 2017-05-29 19:49:28
       History:
 ***********************************************************/
'''
import socket
import time

# 流程：sc (socket -> connect)

# 获取Unix时间戳，用于计时
begin = time.time()

# 创建套接字, 默认参数为：AF_INET、SOCK_STREAM
s = socket.socket()

# 获取主机名称
host = socket.gethostname()
print host
port = 1234

# 连接到服务器的套接字
s.connect((host, port))

# 接收数据
while True:
    string = s.recv(1024)
    if len(string) > 0:
        print string
    else:
        break
end = time.time()
print end - begin
