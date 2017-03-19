# -*- coding: utf-8 -*-

"""
@author: Jie Yin
@e-mail: mumingv@163.com
@date:   2017-03-19
""" 

"""
函数定义与调用
"""
def hello(name):
    return 'Hello, ' + name + '!';

print hello('Jay');


"""
位置参数收集
"""
def printPositionParams(*params):
    print params

printPositionParams(1, 2, 3)


"""
关键字参数收集
"""
def printKeywordParams(**params):
    print params

printKeywordParams(foo = 1, bar = 2, test = 3)


"""
混合参数收集
"""
def printCompoundParams(title, *posParams, **keyParams):
    print title
    print posParams
    print keyParams

printCompoundParams('Params test:', 1, 2, 3, foo = 4, bar = 5, test = 6)


"""
调用函数时使用元组作为实参
"""
def add(x, y):
    return x + y

params = (1, 2)
print add(*params)


"""
调用函数时使用字典作为实参
"""
def hello2(name='Guy', greeting='Welcome'):
    print greeting + ' ' + name + '!';

params = {'name': 'Jay', 'greeting': 'Hello'}
hello2(**params)
