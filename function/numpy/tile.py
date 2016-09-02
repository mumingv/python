# -*- coding: utf-8 -*-
'''
/***********************************************************
      FileName: tile.py
          Desc: 构造二维数组(元素可以是单个数值，也可以是一维数组或二维数组)
        Author: Jie Yin
         Email: mumingv@163.com
      HomePage: https://github.com/mumingv
       Version: 0.0.1
    LastChange: 2016-09-01 21:52:23
       History:
 ***********************************************************/
'''

# syntax: tile()
# http://scipy.github.io/old-wiki/pages/Numpy_Example_List.html#tile.28.29

from numpy import *

# 元素是单个数值
v = 3
a = tile(v, (3, 2))
print(a)
'''
[[3 3]
 [3 3]
 [3 3]]
'''

# 元素是一维数组
v = array([10, 20])
a = tile(v, (3, 2))
print(a)
'''
[[10 20 10 20]
 [10 20 10 20]
 [10 20 10 20]]
'''

# 元素是二维数组
v = array([[10, 20], [30, 40]])
a = tile(v, (3, 2))
print(a)
'''
[[10 20 10 20]
 [30 40 30 40]
 [10 20 10 20]
 [30 40 30 40]
 [10 20 10 20]
 [30 40 30 40]]
'''

