# -*- coding: utf-8 -*-
'''
/***********************************************************
      FileName: sorted.py
          Desc: 给列表/字典等数据结构进行排序
        Author: Jie Yin
         Email: mumingv@163.com
      HomePage: https://github.com/mumingv
       Version: 0.0.1
    LastChange: 2016-08-31 21:11:36
       History:
 ***********************************************************/
'''

# syntax: sorted(iterable[, cmp[, key[, reverse]]])
# https://docs.python.org/2/library/functions.html#sorted
# https://docs.python.org/2/howto/sorting.html#sortinghowto

import operator

# 示例: 给列表进行排序
a = [5, 2, 3, 1, 4]
a = sorted(a)
print(a)  # [1, 2, 3, 4, 5]

# 示例: 给字典进行排序(默认按照key进行排序)
a = {1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}
a = sorted(a)
print(a)  # [1, 2, 3, 4, 5]
a = {1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}
a = sorted(a.iteritems(), key = operator.itemgetter(0))
print(a)  # [(5, 'A'), (2, 'B'), (3, 'B'), (1, 'D'), (4, 'E')]

# 示例: 给字典进行排序(安照value进行排序)
a = {1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}
a = sorted(a.iteritems(), key = operator.itemgetter(1))
print(a)  # [(5, 'A'), (2, 'B'), (3, 'B'), (1, 'D'), (4, 'E')]

# 示例: 给字典进行排序(安照value进行排序, 并且将结果倒序)
a = {1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}
a = sorted(a.iteritems(), key = operator.itemgetter(1), reverse = True)
print(a)  # [(4, 'E'), (1, 'D'), (2, 'B'), (3, 'B'), (5, 'A')]

