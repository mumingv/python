# -*- coding: UTF-8 -*-
'''
/***********************************************************
      FileName: server.py
          Desc: 异步IO: select示例
        Author: Jie Yin
         Email: mumingv@163.com
      HomePage: https://github.com/mumingv
       Version: 0.0.1
    LastChange: 2017-05-30 13:55:40
       History:
 ***********************************************************/
'''
# 源码参考：http://www.cnblogs.com/coser/archive/2012/01/06/2315216.html

import select
import socket
import Queue
import time
 
# 创建一个套接字
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置套接字为非阻塞模式
server.setblocking(1)

# 设置地址重用，以解决如下问题：
# socket.error: [Errno 98] Address already in use
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 
# 绑定IP和端口号到套接字
server_address= ('',10001)
server.bind(server_address)
 
# 启动侦听
server.listen(10)
 
# 构造select函数的第1个参数：为输入而观察的文件/套接字/管道对象列表
inputs = [server]
 
# 构造select函数的第2个参数：为输出而观察的文件/套接字/管道对象列表
outputs = []
 
#Outgoing message queues (socket:Queue)
# 消息队列
message_queues = {}

# select函数的超时时间，单位：秒
timeout = 20

# 输入套接字为空则退出循环
while inputs:
    print "waiting for next event"
    # select函数的第3个参数为异常而观察的文件/套接字/管道对象列表 
    # 说明：
    # 1. 客户端发起连接、发送数据、关闭连接时, select返回的readable都有对应的套接字;
    # 2. outputs不为空就肯定会作为返回值返回;
    readable, writable, exceptional = select.select(inputs, outputs, inputs, timeout)
 
    # select超时会返回三个空列表
    if not (readable or writable or exceptional) :
        print "Time out!"
        break;

    # 先检查有没有发送的数据
    for s in writable:
        try:
            print 'try to send data' 
            next_msg = message_queues[s].get_nowait()
        except Queue.Empty:
            print " " , s.getpeername() , 'queue empty'
            outputs.remove(s)
        else:
            print " sending " , next_msg , " to ", s.getpeername()
            s.send(next_msg)

    # 再检查有没有接收的数据
    for s in readable:
        if s is server:  # 检测到一个客户端连接
            # accept创建一个与客户端连接的套接字，用于接收和发送数据
            connection, client_address = s.accept()
            print "    connection from ", client_address
            connection.setblocking(1)
            # 将accept创建的套接字加入select的轮询列表inputs中
            inputs.append(connection)
            # 给每个创建的套接字申请一个消息队列
            message_queues[connection] = Queue.Queue()
        else: # 检测到一个客户端发送了数据
            data = s.recv(1024)
            #time.sleep(3)
            if data:  # 客户端发送了数据
                print " received " , data , "from ", s.getpeername()
                # 将接收到的消息存放到消息队列
                message_queues[s].put(data)
                # 将套接字存入select的轮询列表outputs中
                if s not in outputs:
                    outputs.append(s)
            else:  # 客户端关闭了TCP连接
                # 没有
                print "  closing", client_address
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                # 删除套接字对应的消息队列
                del message_queues[s]

    for s in exceptional:
        print " exception condition on ", s.getpeername()
        # 异常停止监听
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        # 异常删除消息队列
        del message_queues[s]
