# -*- coding: utf-8 -*-

"""
@author: Jie Yin
@e-mail: mumingv@163.com
@date:   2017-03-19
""" 

# isinstance - 检查对象是否为类的一个实例
# syntax: isinstance(object, classinfo)
# https://docs.python.org/2.7/library/functions.html#isinstance


obj = (1, 2, 3)
if isinstance(obj, tuple):
    print 'true'
else:
    print 'false'

