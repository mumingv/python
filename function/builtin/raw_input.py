# -*- coding: utf-8 -*-

"""
@author: Jie Yin
@e-mail: mumingv@163.com
@date:   2016-03-18
""" 

# raw_input - 获取用户的输入
# syntax: raw_input([prompt])
# https://docs.python.org/2.7/library/functions.html?highlight=input#raw_input

# 不带提示信息
## str1 = raw_input()
# 带提示信息
## str1 = raw_input("Please raw_input: ")

# raw_input会将用户的输入当作一个字符串, 返回值就是该字符串
str1 = raw_input("Please raw_input: ") #如果输入：2+3
print "Your raw_input is:", str1 #打印：2+3
str1 = raw_input("Please raw_input: ") #如果输入：abc123+456
print "Your raw_input is:", str1 #打印：abc123+456

# 和input的区别参考input函数

