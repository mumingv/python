# -*- coding: utf-8 -*-
'''
/***********************************************************
      FileName: zeros.py
          Desc: 创建元素值全为0的数组
        Author: Jie Yin
         Email: mumingv@163.com
      HomePage: https://github.com/mumingv
       Version: 0.0.1
    LastChange: 2016-09-01 11:24:18
       History:
 ***********************************************************/
'''

# syntax: zeros()
# http://scipy.github.io/old-wiki/pages/Numpy_Example_List.html#zeros.28.29

from numpy import zeros

# 示例: 创建元素值全为0的一维数组(下面两种写法都是可以的)
a = zeros(5)
print(a)  # [ 0.  0.  0.  0.  0.]
a = zeros((5))
print(a)  # [ 0.  0.  0.  0.  0.]

# 示例: 创建元素值全为0的一维数组(指定元素类型为int64)
a = zeros(5, int)
print(a)  # [0 0 0 0 0]

# 示例: 创建元素值全为0的二维数组
a = zeros((3, 5))  # 不能写成: zeros(3, 5), 因为参数间以逗号分隔，第二个参数是指元素类型
print(a)
'''
[[ 0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.]]
'''

# 示例: 创建元素值全为0的二维数组，并指定元素类型(int64)
a = zeros((3, 5), int)  # 不指定类型的话，默认元素类型为float64
print(a)
'''
[[0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]]
'''

