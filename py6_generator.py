#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

############################################################
# 生成器
############################################################

# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
L = [x*x for x in range(10)]
G = (x*x for x in range(10))
# 如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值
# 没有更多的元素时，抛出StopIteration的错误
# print(next(G))
# for x in G:
	# print(x)



# 斐波那契数列
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def feibo(max):
	n,a,b = 0,0,1
	while n<max:
		# print(b)
		yield b
		a,b =b,a+b
		n=n+1
	return 'done'
# k = feibo(5)
# for x in k:
# 	print(x)


# 杨辉三角
def triangle(n):
	L=[1]
	while len(L) <= n:
	    yield L
	    L = [1]+[L[x]+L[x+1] for x in range(0,len(L)-1)]+[1]
for x in triangle(5):
	print(x)

# print([1]+[2])