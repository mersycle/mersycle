#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

###############################################################################
# 列表生成式
###############################################################################



# 要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))
# L = list(range(1,11))

# 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
L = []
for x in range(1,11):
	L.append(x*x)

# 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
# 在列表中写出要生成列表的规则
# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
L = [x*x for x in range(1,11)]

# for循环后面还可以加上if判断
L = [x*x for x in range(1,11) if x%2==0]


# 还可以使用两层循环，可以生成全排列
L = [n+m for n in "ABC" for m in '123']
# print(L) # ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']


# 列出当前目录下的所有文件和目录名
import os
dirname = [d for d in os.listdir('.')]
# print(dirname)


# 列表生成式也可以使用两个变量来生成list
d = {'a':"A",'b':"B",'c':"C"}
L = [a+'->'+b for a,b in d.items()]
# print(L)


# 把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
L = [a.lower() for a in L]
# print(L)


L = ['Hello', 'World', 'IBM', 'Apple',18,None]
L = [s.lower() for s in L if isinstance(s,str)]
print(L)