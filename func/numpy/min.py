# -*- coding: utf-8 -*-
'''
/***********************************************************
      FileName: min.py
          Desc: 查询数组中的最小值(包括：二维数组按行或按列查询最小值)
        Author: Jie Yin
         Email: mumingv@163.com
      HomePage: https://github.com/mumingv
       Version: 0.0.1
    LastChange: 2016-09-01 21:29:00
       History:
 ***********************************************************/
'''

# syntax: min()
# http://scipy.github.io/old-wiki/pages/Numpy_Example_List.html#min.28.29

from numpy import *

# 查询一维数组最小值
a = array([10, 20, 30])
print(a.min())  # 10

# 查询二维数组最小值
a = array([[10, 50, 30], [60, 20, 40]])
print(a.min())  # 10

# 查询二维数组每一列的最小值(两种写法等价)
a = array([[10, 50, 30], [60, 20, 40]])
print(a.min(axis = 0))  # [10 20 30]
print(a.min(0))  # [10 20 30]

# 查询二维数组每一行的最小值(两种写法等价)
a = array([[10, 50, 30], [60, 20, 40]])
print(a.min(axis = 1))  # [10 20]
print(a.min(1))  # [10 20]

# min(a)只能用于一维数组
a = array([10, 20, 30])
b = min(a)
print(b)  # 10

