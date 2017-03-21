# -*- coding: utf-8 -*-

"""
@author: Jie Yin
@e-mail: mumingv@163.com
@date:   2017-03-19
""" 

"""
类的定义与使用
"""
class Person:
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def sayHello(self):
        print "Hello, world! I'm %s." % self.name

foo = Person()
foo.setName('Jay')
foo.sayHello()


"""
类的构造函数
"""
class ListNode(object):
    def __init__(self, x): 
        self.val = x 
        self.next = None

node = ListNode(0)
print node.val
print node.next
