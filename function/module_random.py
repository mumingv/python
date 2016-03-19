# -*- coding: utf-8 -*-

"""
@author: Jie Yin
@e-mail: mumingv@163.com
@date:   2016-03-19
""" 

# 伪随机数函数
# https://docs.python.org/2.7/library/random.html
# 注：之所以叫伪随机数，是因为对于同一个随机种子，生成的随机序列是固定不变的. 

# +---------------------------+--------------------------------------------+
#   随机数函数                  含义
# +---------------------------+--------------------------------------------+
#   random.seed(x)              给随机数一个种子值，默认随机种子是系统时钟
#   random.random()             生成一个[0, 1.0]之间的随机小数
#   random.uniform(a, b)        生成一个a到b之间的随机小数
#   random.randint(a, b)        生成一个a到b之间的随机整数, 包含a和b
#   random.randrange(a, b, c)   生成一个a到b之间的以c递增的随机数
#   random.shuffle(<list>)      将列表中的元素打乱, 无返回值
#   random.choice(<list>)       从列表中随机获取一个元素
#   random.sample(<list>, k)    从列表中随机获取k个元素的列表
# +---------------------------+--------------------------------------------+

# 示例
import random
print "seed:", random.random()  #输出：0.688808497408, 0.591582132332, 0.373279611256
print "uniform:", random.uniform(1, 3)  #输出：2.68467386773
print "randint:", random.randint(1, 3)  #输出：1, 2, 3
print "randrange:", random.randrange(1, 10, 3)  #输出：1, 4, 7
list1 = range(10)
print list1
random.shuffle(list1)
print "shuffle:", list1  #输出：[4, 0, 9, 1, 6, 2, 5, 7, 3, 8]
print "choice:", random.choice(list1)  #输出：9
print "sample:", random.sample(list1, 3)  #输出：[9, 1, 0]

# 同一个随机种子对应的随机序列是一致的
random.seed(10)
print "uniform:", random.uniform(1, 10)
print "uniform:", random.uniform(1, 10)
random.seed(10)
print "uniform2:", random.uniform(1, 10)
print "uniform2:", random.uniform(1, 10)

