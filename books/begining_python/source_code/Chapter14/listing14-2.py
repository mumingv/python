'''
/***********************************************************
      FileName: listing14-2.py
          Desc: 
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

begin = time.time()
s = socket.socket()

host = socket.gethostname()
port = 1234

s.connect((host, port))
print s.recv(1024)
end = time.time()
print end - begin
