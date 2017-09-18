#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

###################################################################
# 迭代器
###################################################################

# 可以直接作用于for循环的数据类型有以下几种：
# 一类是集合数据类型，如list、tuple、dict、set、str等；
# 一类是generator，包括生成器和带yield的generator function。
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
# 可以使用isinstance()判断一个对象是否是Iterable对象：
from collections import Iterable,Iterator
# print(isinstance([],Iterable))
# print(isinstance('abc',Iterable))



# 而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
# 可以使用isinstance()判断一个对象是否是Iterator对象：
# print(isinstance(list(range(1,10)),Iterator))
# print(isinstance((x for x in range(1,10)),Iterator))



# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
# print(isinstance(iter([]),Iterator))


# map()
# map()函数接收两个参数，一个是函数，一个是Iterable
def f(x):
	return x*x

r = map(f,[1,2,12,3])
# print(list(r))
# print(list(map(str,[1,2,3])))


# reduce()
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce
def add(x,y):
	return x+y
r = reduce(add,[1,3,4])
r = sum([1,3,4])



# 但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场
def fn(x,y):
	return x*10+y
r = reduce(fn,[1,3,5,7,9])




# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
# def normalize(x):
# 	L = []
# 	for a in x:
# 		a = upper(a[0])
# 		a_o = lower(a[1,len(a)])
# 		new_a = a+a_o
# 		L.append(new_a)
# r = list(map(normalize,['adam', 'LISA', 'barT']))
r = 'aaa'
print(r[0])