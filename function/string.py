# -*- coding: utf-8 -*-

"""
@author: Jie Yin
@e-mail: mumingv@163.com
@date:   2016-03-18
""" 

# 字符串操作

# +---------------------------+--------------------------------------------+
#   字符串操作函数              含义
# +---------------------------+--------------------------------------------+
#   <string>.upper()            字符串中字母大写
#   <string>.lower()            字符串中字母小写
#   <string>.capitalize()       首字母大写
#   <string>.strip()            去除两边空格及指定字符
#   <string>.split()            按指定字符分割字符串为数组/列表, 分割字符默认为空格
#   <string>.isdigit()          判断是否是数字类型, 是返回True，否返回False 
#   <string>.find()             搜索指定字符串
#   <string>.replace()          字符串替换 

# 示例
vlist = "Python is an excellent language".split()
print vlist  #输出：['Python', 'is', 'an', 'excellent', 'language']

