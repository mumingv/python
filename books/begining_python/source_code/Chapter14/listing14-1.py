# -*- coding: UTF-8 -*-
'''
/***********************************************************
      FileName: listing14-1.py
          Desc: 服务器
        Author: Jie Yin
         Email: mumingv@163.com
      HomePage: https://github.com/mumingv
       Version: 0.0.1
    LastChange: 2017-05-29 19:48:26
       History:
 ***********************************************************/
'''
import socket
import time

# 流程：sbla (socket -> bind -> listen -> accept)

# 创建套接字, 默认参数为：AF_INET、SOCK_STREAM
s = socket.socket()

# 获取主机名称
host = socket.gethostname()
port = 1234

# 绑定主机名和端口号
s.bind((host, port))

# 开始侦听
s.listen(20)  # 实际队列中的最大连接数比配置的backlog要多一个, 如果backlog为1, 则客户端同时发送3个请求也能够处理
while True:
    # c是新建的socket对象，用于发送数据给客户端；addr是客户端的IP地址和端口号
    c, addr = s.accept()
    print 'Got connection from', addr
    # 延迟5秒
    time.sleep(5)
    # 使用新建的socket对象发送数据 
    dataLength = c.send('Thank you for connecting')
    print 'Sent data length is:', dataLength
    # 关闭新建的socket 
    c.close()
