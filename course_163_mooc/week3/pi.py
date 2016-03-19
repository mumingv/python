# -*- coding: utf-8 -*-

"""
@author: Jie Yin
@e-mail: mumingv@163.com
@date:   2016-03-19
""" 

# 使用蒙特卡洛方法计算pi值

# 蒙特卡洛(Monte Carlo)方法，又称为随机抽样或统计试验方法。当所求解的问题是某种事件出现的概率，或某随机变量的期望值时，可以通过某种“实验”的方法求解。
# 简单说，蒙特卡洛方法是利用随机试验求解问题的方法。

# 求解方法
# 设置边长1*1的正方形，以正方形的其中一个顶点为圆心、边长1为半径作1/4圆，向该正方形中随机抛撒点，则落在1/4圆中的点的数量除以总的抛撒点的数量就是1/4圆和正方形的面积比(pi/4)。

import math
import random
import time

DARTS = 1000000  #抛撒点的总数量
hit_num = 0  #落在1/4圆中的抛撒点的数量

for i in range(DARTS):
    # 生成两个0到1之间的随机数, 表示该抛撒点的坐标x和y
    x, y = random.random(), random.random()
    # 计算该抛撒点到1/4圆的圆心之间的距离
    distance = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    # 如果计算的距离小于1，则表示该抛撒点落在该1/4圆内
    if distance <= 1:
        hit_num += 1

# 计算pi值
pi = 4 * (float(hit_num) / DARTS)
print "Pi is:", pi
print "Time is:", time.clock(), "s"






