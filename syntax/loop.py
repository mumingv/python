# -*- coding: utf-8 -*-

"""
@author: Jie Yin
@e-mail: mumingv@163.com
@date:   2017-03-14
""" 

"""
for循环
"""

# 遍历字符串
string = 'Hello'
for c in string:
    print c

# 遍历字符串列表
words = ['this', 'is', 'python', 'note']
for word in words:
    print word

# 遍历数字列表
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    print number

for number in range(0, 10):
    print number

# 遍历字典
dict = {'x': 1, 'y': 2, 'z': 3}
for key in dict:
    print key, 'corresponds to', dict[key]


"""
while循环
"""
print '-----while-----'
x = 1
while x < 10:
    print x
    x += 1

