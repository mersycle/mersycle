#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

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
def normalize(a):
	a_o = a[1:len(a)].lower()
	a = a[0].upper()
	new_a = a+a_o
	return new_a
r = list(map(normalize,['adam', 'LISA', 'barT']))

def normalize2(x):
	L = []
	for a in x:
		new_f = a[0].upper()
		new_l = a[1:len(a)].lower()
		new_a = new_f+new_l
		L.append(new_a)
	return L
r = ['adam', 'LISA', 'barT']
r = normalize2(r)




# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(x,y):
	return x*y
r = reduce(prod,[1,3,4,5,2])



# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def str2float(s):
	def char2num(ss):
		return{'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[ss]
	def fn(x,y):
		return (10*x+y)
	L = s.split('.')
	if L[0][0] != "-":
		a1 = reduce(fn,map(char2num,L[0]))
		a2 = reduce(fn,map(char2num,L[1]))
		b = len(L[1])
		a = a1+(0.1**b)*a2
	else:
		L[0] = L[0][1:]
		a1 = reduce(fn,map(char2num,L[0]))
		a2 = reduce(fn,map(char2num,L[1]))
		b = len(L[1])
		a = -a1-(0.1**b)*a2
	return a

print('str2float(\'123.456\')',str2float('123.456'))