#!/usr/bin/evn python3
# -*- coding: utf-8 -*-


############################################
# filter
############################################

# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素



# 在一个list中，删掉偶数，只保留奇数
def is_odd(n):
	return n % 2 == 1
s = list(filter(is_odd,[1,2,3,4,5,6]))
# print(s)

# 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。


# 用filter求素数

# 计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：
# 首先，列出从2开始的所有自然数，构造一个序列：
# 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
# 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
# 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
# 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 不断筛下去，就可以得到所有的素数。

# 用Python来实现这个算法，可以先构造一个从3开始的奇数序列：
def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

# 筛选函数
def _not_divisible(n):
	return lambda x: x % n > 0

# 定义一个生成器，不断返回下一个素数：
def primes():
	yield 2
	it = _odd_iter() # 初始化序列
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n),it)

# 这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列。
# 由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：
# for n in primes():
# 	if n < 100:
# 		print(n)
# 	else:
# 		break


def is_palindrome(n):
	return str(n) == str(n)[::-1] and len(str(n))>1
output = filter(is_palindrome,range(1,1000))
print(list(output))