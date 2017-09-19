#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#########################################
# sorted 排序
#########################################

sorted([36, 5, -12, 9, -21]) # [-21, -12, 5, 9, 36]

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
r = sorted([36, 5, -12, 9, -21],key=abs)
# print(r) #[5, 9, -12, -21, 36]

# 字符串排序
# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面
r = sorted(['bob', 'about', 'Zoo', 'Credit'])
# print(r) # ['Credit', 'Zoo', 'about', 'bob']

# 统一成小写
r = sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower)
# print(r) # ['about', 'bob', 'Credit', 'Zoo']

# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
r = sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True)
# print(r) # ['Zoo', 'Credit', 'bob', 'about']



L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return t[0]
def by_score(t):
	return t[1]
L2 = sorted(L, key=by_name)
L3 = sorted(L, key=by_score,reverse=True)
print(L2)
print(L3)