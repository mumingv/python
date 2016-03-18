# -*- coding: utf-8 -*-

"""
@author: Jie Yin
@e-mail: mumingv@163.com
@date:   2016-03-18
""" 

# range - 生成一个由整数组成的List
# syntax1: range(stop)
# syntax2: range(start, stop[, step])
# https://docs.python.org/2.7/library/functions.html#range

# 对于参数个数, 如果
# 只有一个参数，则对应range(stop)
# 有两个参数，则对应range(start, stop)
# 有三个参数，则对应range(start, stop, step)

# 对于参数取值
# start，可选参数，默认值为0；
# stop，必选参数，无默认值；
# step，可选参数，默认值为1，可以为负数，但不能为0；

# range函数生成的List中，不包含stop;

# range函数一般用作for循环中, 如:
for i in range(3):
    print i  #打印: 0 1 2

# 一些示例
list1 = range(10)
print list1  #打印: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = range(3, 10)
print list2  #打印: [3, 4, 5, 6, 7, 8, 9]
list3 = range(3, 10, 3)
print list3  #打印: [3, 6, 9]
list4 = range(3, 9, 3)
print list4  #打印: [3, 6]

# step为负数的一些示例
list10 = range(9, -3, -1)
print list10  #打印: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2]

# 一些特别的示例
list20 = range(0)  #range(0)和range(0, 0)等价
print list20  #打印: []
list21 = range(1, 0)  #range(1, 0)和range(1, 0, 1)等价
print list21  #打印: []

# 异常示例
list30 = range(1, 10, 0)  #step不能为0，为0的话就永远到不了stop了
print list30  #提示错误: "ValueError: range() step argument must not be zero"

