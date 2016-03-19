# -*- coding: utf-8 -*-

"""
@author: Jie Yin
@e-mail: mumingv@163.com
@date:   2016-03-19
""" 

# len - 返回对象的长度
# syntax: len(s)
# https://docs.python.org/2.7/library/functions.html#len

# 示例
#print len(3)  #输出错误："TypeError: object of type 'int' has no len()"
print len("abc")  #输出：3
print len("老师好")  #输出：python2.x为6或者9(是编码不同而不同)，python3.x为3
print len([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])  #输出：10

