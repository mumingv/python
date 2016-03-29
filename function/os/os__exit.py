# -*- coding: utf-8 -*-
'''
/***********************************************************
      FileName: os__exit.py
          Desc: 退出系统 
        Author: Jie Yin
         Email: mumingv@163.com
      HomePage: https://github.com/mumingv
       Version: 0.0.1
    LastChange: 2016-03-29 19:53:59
       History:
 ***********************************************************/
'''

# 语法：os._exit(n)
# 说明：该方法通常用于退出子进程

# 示例
import os

print "Hello"
os._exit(os.EX_DATAERR)
print "world"

