# -*- coding: utf-8 -*-

"""
@author: Jie Yin
@e-mail: mumingv@163.com
@date:   2016-03-18
""" 

# 输入数字1-7，返回星期一到星期日

weekday = "MonTueWedThuFriSatSun"
user_input = int(raw_input("请输入[1-7]范围内的一个数字："))
if user_input < 1 or user_input > 7:
    print "Input error, please try again!"
    exit()  #这里调用的是函数, 不能不加括号
start_pos = (user_input - 1) * 3 
end_pos = start_pos + 3
print "对应的日子是:", weekday[start_pos:end_pos]

