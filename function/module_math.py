# -*- coding: utf-8 -*-

"""
@author: Jie Yin
@e-mail: mumingv@163.com
@date:   2016-03-19
""" 

# 数学函数
# https://docs.python.org/2.7/library/math.html

# +---------------------------+--------------------------------------------+
#   数学函数                    含义
# +---------------------------+--------------------------------------------+
#   math.pi                     常量，圆周率pi = 3.1415926...
#   math.e                      常量，自然常数e = 2.718281...
#   math.ceil(x)                对浮点数x向上取整, 返回值>=x
#   math.floor(x)               对浮点数x向下取整, 返回值<=x
#   math.pow(x, y)              计算x的y次方
#   math.sqrt(x)                计算x的平方根, 返回一个浮点数
#   math.log(x)                 以e为底的对数
#   math.log10(x)               以10为底的对数
#   math.exp(x)                 计算e的x次幂 
#   math.degrees(x)             将弧度转换为角度 
#   math.radians(x)             将角度转换为弧度
#   math.sin(x)                 正弦函数
#   math.cos(x)                 余弦函数
#   math.tan(x)                 正切函数
#   math.asin(x)                反正弦函数
#   math.acos(x)                反余弦函数
#   math.atan(x)                反正切函数
# +---------------------------+--------------------------------------------+

# 示例
import math
print "pi =", math.pi  #输出：pi = 3.14159265359
print "e =", math.e  #输出：e = 2.71828182846
print math.ceil(3.14)  #输出：4.0
print math.ceil(4)  #输出：4.0
print math.ceil(-3.14)  #输出：-3.0
print math.floor(3.14)  #输出：3.0
print math.floor(4)  #输出：4.0
print math.floor(-3.14)  #输出：-4.0
print "pow:", math.pow(2, 3)  #输出：8.0
print "sqrt:", math.sqrt(4)  #输出：2.0
print "log:", math.log(math.e)  #输出：1.0
print "log10:", math.log10(10)  #输出：1.0
print "exp:", math.exp(2)  #输出：7.38905609893
print "degrees:", math.degrees(math.pi)  #输出：180.0
print "radians:", math.radians(360)  #输出：6.28318530718
print "sin:", math.sin(0)  #输出：0.0
print "cos:", math.cos(0)  #输出：1.0
print "tan:", math.tan(0)  #输出：0.0
print "asin:", math.asin(1)  #输出：1.57079632679(pi/2)
print "acos:", math.acos(1)  #输出：0.0
print "atan:", math.atan(1)  #输出：0.785398163397(pi/4)

