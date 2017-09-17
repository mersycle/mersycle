# -*- coding: utf-8 -*-

# 引入内置数学函数
import math

# 定义一个取绝对值的函数
def my_abs(x):
	# 没有指定x数值类型 当输入参数为字符串时 报类型错误,对参数类型做检查，只允许整数和浮点数类型的参数
	if not isinstance(x,(int,float)):
		return '只能输入整型和浮点型'
	if x >= 0:
		return x
	else:
		return -x
# 若是在python解释器下调用该函数，可使用 from py_funtion import my_abs
# print(my_abs('aaa'))

# 返回多个值函数
def move(x,y,setp,angle=0):
	nx = x + setp*math.cos(angle)
	ny = x - setp*math.sin(angle)
	return nx,ny

# print(move(100,100,60,math.pi/6))
r = move(100,100,60,math.pi/6)
# print(r) #其实返回的是tuple
# print(r[0])
# print(type(r))


# 定义一个计算x的n次方函数 power是内置函数 计算平方的
def power(x,n=2):
	# 判断一下参数类型
	if not isinstance(x,(int,float)):
		return '参数x类型错误'
	if not isinstance(n,(int,float)):
		return '参数n类型错误'
	s = 1
	while n>0:
		s = x*s
		n = n-1
	return s

# print(power(4))
# print(power(44,3))


# 定义一个函数 默认参数为list
def add_end(l=[]):
	l.append('end')
	return l
# print(add_end())
# print(add_end())

# 修改add_end
def add_end1(l=None):
 	if l is None:
 		l = []
 	l.append('end')
 	return l
# print(add_end1())
# print(add_end1())


# 可变参数 a^2+b^2+c^...
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n*n
	return sum
# print(calc(1,2,3)) #14
# print(calc(*[1,2,3])) #14 需要加个*
# print(calc(*(1,2,3))) #14 需要加个*


# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)
# person('zhangsan',14) # name: zhangsan age: 14 other: {}
# person('zhangsan',14,city="beijing") # name: zhangsan age: 14 other: {'city': 'beijing'}
# extra = {'city':'beijing','job':'banzhuan'}
# person('zhangsan',14,**extra) # name: zhangsan age: 14 other: {'city': 'beijing', 'job': 'banzhuan'}



# 参数组合

# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

# 比如定义一个函数，包含上述若干种参数：
def ff(a,b,c=0,*args,**kw):
	print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
# ff(1,2)
# ff(1,2,3)
# ff(1,2,3,4,5,6,7,7) # a= 1 b= 2 c= 3 args= (4, 5, 6, 7, 7) kw= {}
# ff(1,2,3,45,6,7,7,kw='kw') # a= 1 b= 2 c= 3 args= (45, 6, 7, 7) kw= {'kw': 'kw'}
args=(1,2,3,4)
kw={'kw':'kw'}
ff(*args,**kw)

# 要注意定义可变参数和关键字参数的语法：

# *args是可变参数，args接收的是一个tuple；

# **kw是关键字参数，kw接收的是一个dict。

# 以及调用函数时如何传入可变参数和关键字参数的语法：

# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。