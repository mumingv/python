# -*- coding: utf-8 -*-
'''
/***********************************************************
      FileName: split.py
          Desc: 按指定字符分割字符串为数组/列表, 分割字符默认为空白字符(空格、TAB、换行、回车、formfeed)
        Author: Jie Yin
         Email: mumingv@163.com
      HomePage: https://github.com/mumingv
       Version: 0.0.1
    LastChange: 2016-09-01 14:40:07
       History:
 ***********************************************************/
'''

# syntax: string.split(s[, sep[, maxsplit]])

# 示例：按空格将字符串分割成列表
list = "Python is an excellent language".split()
print list  # ['Python', 'is', 'an', 'excellent', 'language']

# 示例：按TAB将字符串分割成列表
list = "Python	is	an	excellent	language".split('\t')
print list  # ['Python', 'is', 'an', 'excellent', 'language']

