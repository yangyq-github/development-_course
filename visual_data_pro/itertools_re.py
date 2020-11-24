#!/usr/bin/python3
# coding : utf-8
# @Time  : 2020/11/23 10:06
# @File  : itertools_re.py
__author__ = 'yangyanqin'
"""对itertools模块的学习"""

import itertools

n = itertools.count(step=2)
# count:创建一个迭代器，生成从n开始的连续整数，如果不设置start，则默认从0开始，step是步长，不支持长整型

# for i in n:
#     if i >100:
#         break
#     print(type(i))

a = itertools.cycle("abd")
# cycle:传入一个序列，无线循环下去
# for i in a:
#     print(i)

b =itertools.repeat('123',times=3)
# repeat:创建一个迭代器，重复生成object，times可以设置指定重复次数
# for i in b:
#     print(i)


c= itertools.chain("234","444")
# chain:将多个迭代器作为参数，但只返回单个迭代器，将产生所有参数迭代器的内容，好像来自一个单一的序列

# for i in c:
#     print(i)

d= itertools.groupby("addfafdfdfd")

# for key,value in d:
#     print(key,list(value))

a=([1, 4, 3,8], [3, 2, 5,5], [5, 1, 2,9], [4, 3, 1,0], [2, 5, 3,6])
# print(a.index("xyz"))
# print(sorted(a,key=lambda __:__[3]))
b=[*zip(*a)]

a = [(1, 7175),(10, 8504),(2, 8504)]
print(sorted(a,key=lambda __:__[0]))



