# -*- coding: utf-8 -*-

"""
@author: mumingv@163.com
@date:   2016-03-16
""" 

# 转义字符
print "Hello, I'm Tom."
print "Hello, I\'m Tom."
print 'Hello, I\'m Tom.' #单引号中也可以使用转义字符

# python中的一行就是一条语句，不能写成下面这样: 
"""
print 'Hello
World'
"""

# 将Hello和World两个单词分别输出到两行
## 方法一
print "Hello\nWorld"
## 方法二
print 'Hello\nWorld'
## 方法三
print "Hello"
print "World"

