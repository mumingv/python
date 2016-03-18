# -*- coding: utf-8 -*-

"""
@author: Jie Yin
@e-mail: mumingv@163.com
@date:   2016-03-18
""" 

# 列表/序列操作

# +---------------------------+--------------------------------------------+
#   列表操作函数                含义
# +---------------------------+--------------------------------------------+
#   <list>.append(x)            将元素x增加到列表的最后
#   <list>.sort()               将列表元素排序
#   <list>.reverse()            将列表元素反转
#   <list>.index(x)             返回第一次出现元素x的索引值
#   <list>.insert(i, x)         在位置i处插入新元素x
#   <list>.count(x)             返回元素x在列表中的数量
#   <list>.remove(x)            删除列表中第一次出现的元素x
#   <list>.pop(i)               取出列表中位置i的元素并删除它

# 示例
vlist = [0, 1, 2, 3, 4]
print vlist  #输出：[0, 1, 2, 3, 4]
vlist.append("python")
print vlist  #输出：[0, 1, 2, 3, 4, 'python']
vlist.reverse()
print vlist  #输出：['python', 4, 3, 2, 1, 0]











