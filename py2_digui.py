# -*- coding:utf-8 -*-

# 递归函数
def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)
# print(fact(5))
# n=5 5*fact(4)
# n=4 5*4*fact(3)
# n=3 5*4*3*fact(2)
# n=2 5*4*3*2*fact(1)
# n=1 5*4*3*2*1


# 尾递归
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况，上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了。要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中：
def nfact(n):
	return fact_iter(n,1)

def fact_iter(num,product):
	if num==1:
		return product
	return fact_iter(num-1,num*product)
# print(nfact(5))


# 递归实现汉诺塔
def move(n,a,b,c):
	if n==1:
		print(a+'->'+c)
	else:
		move(n-1,a,c,b)
		move(1,a,b,c)
		move(n-1,b,a,c)
# move(int(input('层数')),'A','B','C')


# 构建一个1,3,5,...,99列表
def make():
	lista = []
	n = 1
	while n<=99:
		lista.append(n)
		n = n + 2
	return lista
# print(make())