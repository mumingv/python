# -*- coding: utf-8 -*-
'''
/***********************************************************
      FileName: get.py
          Desc: 根据key获取value
        Author: Jie Yin
         Email: mumingv@163.com
      HomePage: https://github.com/mumingv
       Version: 0.0.1
    LastChange: 2016-09-01 15:44:54
       History:
 ***********************************************************/
'''

# syntax: get(key[, default])

# 示例: 根据key获取value
love_dictionary = {'largeDoses': 3, 'smallDoses': 2, 'didntLike': 1}
print love_dictionary.get('smallDoses')  # 2
print love_dictionary.get('NotExist')  # None

