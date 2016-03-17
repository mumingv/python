# -*- coding: utf-8 -*-

"""
@author: Jie Yin
@e-mail: mumingv@163.com
@date:   2016-03-18
""" 

# input - 获取用户的输入
# syntax: input([prompt])
# https://docs.python.org/2.7/library/functions.html?highlight=input#input

# 不带提示信息
## str1 = input()
# 带提示信息
## str1 = input("Please input: ")

# input会将用户的输入当作一个算术表达式, 返回值是一个数值
str1 = input("Please input: ") #如果输入：2+3
print "Your input is:", str1 #打印：5

# input和raw_input的区别
## input返回一个数值，而raw_input返回一个字符串;
## input([prompt]) = eval(raw_input(prompt))
str2 = raw_input("Please raw_input: ") #如果输入：2+3
print "Your raw_input is:", str2 #打印：2+3
str3 = eval(raw_input("Please eval(raw_input): ")) #如果输入：2+3
print "Your eval(raw_input) is:", str3 #打印：5

