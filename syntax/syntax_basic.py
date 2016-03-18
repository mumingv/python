# -*- coding: utf-8 -*-

"""
@author: Jie Yin
@e-mail: mumingv@163.com
@date:   2016-03-16
""" 

"""
注释
"""
# 单行注释：使用#(井号)
# 多行注释：使用一对'''(三个单引号)，或者使用一对"""(三个双引号)包含注释信息


"""
缩进
"""
# 使用缩进表示代码块，不用{}表示代码块


"""
类型
"""
# 数字类型

## 整数类型
### 整数类型没有取值范围的限制。
print "--> 整数类型"
print pow(2, 10)
print pow(2, 1000)
### 整数类型不同进制的表示方法
### 2进制: 0b010, 0B010
### 8进制: 0o123, 0O456
### 16进制: 0x1a, 0X3c

## 浮点数类型
### 查看浮点数的精度
### >>> import sys
### >>> sys.float_info

## 复数类型
### z = a + bj, a和b都是浮点数类型，虚数部分用j或者J表示
### 例子
print "--> 复数类型"
z = 1.23e-4 + 5.6e+89j
print "real is:", z.real, " imag is:", z.imag

## 允许整数、浮点数、复数这三种类型之间进行混合运算，结果为最宽类型

## 可以使用int()、float()、complex()进行各种类型之间的强制转换
### 例子
print int(3.14)  #输出：3
print float(3)  #输出：3.0
print complex(3)  #输出：(3+0j)
#print int(3 + 4j)  #提示错误："TypeError: can't convert complex to int"
#print float(3 + 4j)  #提示错误："TypeError: can't convert complex to float"

## 判断数字类型
print "--> 判断数字类型"
print type(3)  #输出: <type 'int'>
print type(3.14)  #输出: <type 'float'>
print type(3 + 4j)  #输出: <type 'complex'>

## 数字类型的运算
# +--------------------+--------------------------------------------+
#   运算符和运算函数     操作含义
# +--------------------+--------------------------------------------+
#   x + y                和
#   x - y                差
#   x * y                积
#   x / y                商
#   x // y               不大于x与y之商的最大整数
#   x % y                余数
#   +x                   x
#   -x                   x的负值
#   x ** y               x的y次幂
#   abs(x)               x的绝对值 
#   divmod(x, y)         (x // y, x % y) 
#   pow(x, y)            x的y次幂，和x ** y相同 
# +--------------------+--------------------------------------------+
print "--> 数字类型的运算"
print 5 + 3
print 5 - 3
print 5 * 3
print 5 / 3  #输出：1
print 5 // 3  #输出：1
print 5 % 3  #输出：2
print +5  #输出：5
print -5  #输出：-5
print 5 ** 3  #输出：125
print abs(-5)  #输出：5
print divmod(5, 3)  #输出：(1, 2)
print pow(5, 3)  #输出：125


# 字符串类型

## 使用单引号或者双引号均可以表示一个字符串
print "--> 字符串类型"
print "Hello"
print 'world'

## 测试字符串类型
print type("Hello")  #输出：<type 'str'>

## 获取子字符串
print "获取子字符串"
str = "abcdefg"
print str[0:2]  #输出: "ab", 表示区间[0,2)内的子字符串
print str[-1]  #输出: "g", 表示下标为-1的字符
print str[0:-1]  #输出: "abcdef", 表示除最后一个字符外的子字符串
## 可以使用表达式作为下标/索引值
print str[1 + 2]  #输出: "d"
x = 3
print str[x + 1]  #输出："e"

## 字符串连接
## 使用 + 或 * 进行连接
print "--> 字符串连接"
print "Hello" + "World"  #输出：HelloWorld
print 3 * "Hello"  #输出：HelloHelloHello

## 字符串长度
print "--> 字符串长度"
print len("Hello")  #输出：5



# 元组类型
# 列表类型
# 文件类型
# 字典类型

"""
变量
"""
# 命名
## 1. 由字母、数字、下划线组成，且不能以数字开头；
## 2. 中文字符也可以作为变量名称；

# 保留字(共33个), 不能用作变量的名字
## 8个: and as assert break class continue def del
## 8个: elif else except finally for from globall if
## 8个: import in is lambda nonlocal not or pass
## 6个: raise return try while with yield
## 3个: True False None

# 同步赋值
## 含义：指同时给多个变量赋值，即先运算右侧N个表达式，然后同时将表达式结果赋值给左侧对应的变量。
## 语法：<变量1>, <变量2>, ... , <变量N> = <表达式1>, <表达式2>, ... , <表达式N>
## 示例：交换变量x和y的值
print "同步赋值"
x = 2
y = 3
print "交换前: x =", x, ", y =", y
x, y = y, x
print "交换后: x =", x, ", y =", y

"""
数据结构 - List
"""

"""
数据结构 - Tuple
"""

"""
数据结构 - Dict
"""

"""
数据结构 - Set
"""

"""
数据结构 - 总结
"""
# +---------+----------+----------+----------+------------------------+
# +         + 顺序存储 + 内容可变 + 重复元素 +  备注                  +
# +---------+----------+----------+----------+------------------------+
# +  List   +    是    +    是    +    是    +   []                   +
# +---------+----------+----------+----------+------------------------+
# +  Tuple  +    是    +    否    +    是    +   ()                   +
# +---------+----------+----------+----------+------------------------+
# +  Dict   +    否    +    是    +    否    +   {}                   +
# +---------+----------+----------+----------+------------------------+
# +  Set    +    否    +    是    +    否    + set([]), 只有key的Dict +
# +---------+----------+----------+----------+------------------------+

"""
函数
"""

# 函数库引用
## 方式一, 示例:
## >>> import turtle
## >>> turtle.fd(100)
## 方式二, 示例:
## >>> from turtle import *
## >>> from turtle import fd
## >>> fd(100)

"""
类
"""

"""
条件语句
"""

"""
循环语句
"""
# for循环
## 示例
print "循环"
for i in range(3):
    print i

"""
"""

