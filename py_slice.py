#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

# 切片
names = ['zhangsan','lisi','wangwu','niuniu','xiaoma']
# names[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
# print(names[0:3]) #['zhangsan', 'lisi', 'wangwu']
# 如果第一个索引是0，还可以省略
# print(names[:3]) #['zhangsan', 'lisi', 'wangwu']
# 同样支持倒数切片
# print(names[-2:]) #['niuniu', 'xiaoma']




# 0-99的数列
L = list(range(100)) 
# 取前10个数
# print(L[:10])
# 取后10个数
# print(L[-10:])
# 前10个数，每两个取一个
# print(L[:10:2])
# 所有数每5个取一个
# print(L[::5])
# 甚至什么都不写，只写[:]就可以原样复制一个list：
# print(L[:])



# tuple
T = tuple(range(0,10))
print(T[::2])



# string
S = 'ABCDEFG'
print(S[::2])