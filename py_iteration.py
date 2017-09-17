#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

# 迭代
# 在Python中，迭代是通过for ... in来完成的，而很多语言比如C或者Java，迭代list是通过下标完成的Python的for循环抽象程度要高于Java的for循环，因为Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。

# list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代
# 迭代字典
d = {"a":1,"b":2,"c":3}

# 只迭代key
# for key in d:
	# print(key) # 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样(随机)。

# 只迭代value
# print(d.values()) # dict_values([1, 2, 3])
# for value in d.values():
# 	print(value)

# 同时迭代key和value
# for key,value in d.items():
	# print(key,'-----',value)



# 迭代string
s = 'ABCDEFG'
# for v in s:
	# print(v)



# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
# 需要先引入这个模块
from collections import Iterable
a = isinstance('abs',Iterable) # True
b = isinstance([1,2,3],Iterable) # True
c = isinstance(123,Iterable) # False
# print(c)


# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
a = ['a','b','c']
# for k,v in enumerate(a):
# 	print(k,'->',v)


# for x,y in [(1,2),(3,4),(5,6)]:
# 	print(x,'->',y)

# for x,y in enumerate([(1,2),(3,4),(5,6)]):
# 	print(x,'->',y)