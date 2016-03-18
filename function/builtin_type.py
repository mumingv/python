# -*- coding: utf-8 -*-

"""
@author: Jie Yin
@e-mail: mumingv@163.com
@date:   2016-03-18
""" 

# type - 返回对象的类型, 返回值为type object
# syntax1: class type(object)
# syntax2: class type(name, bases, dict)
# https://docs.python.org/2.7/library/functions.html#type

# 示例
## 判断数字类型
print "--> 判断数字类型"
print type(3)  #输出: <type 'int'>
print type(3.14)  #输出: <type 'float'>
print type(3 + 4j)  #输出: <type 'complex'>

