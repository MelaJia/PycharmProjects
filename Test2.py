# -*- coding: utf-8 -*-
def square_of_sum(L):
    sum = 0
    for x in L:
        sum = sum + x * x
    return sum
print square_of_sum([1,2,3,4,5,])

#循环与迭代
#while 迭代
x = 0
while x < 5:
    print x
    x = x + 1
x = 0
while x < 11:
    x += 1
    if x % 2 == 0:
        continue
    print x * x
#for 迭代
for zifu in 'beijinng':
    print zifu
for xingming in ['c','w','l']:
    print xingming.upper()
#对字典进行迭代
xuesheng = {'xiaoming':1,'xiaowang':2,'xiaoli':3}
for xin in xuesheng.keys():
    print xin
for ming in xuesheng.values():
    print ming
for xs in xuesheng.items():
    print xs
for xi,mi in xuesheng.items():
    print xi , mi
# range(start,stop,step)迭代器
# 取前100位的自然数
print range(1, 101)
#取出10以内的偶数    [0, 2, 4, 6, 8]
print range(0,10,2)
#倒数10到1 [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print range(10,0,-1)


#函数
def da():
    print 'ok!'
da()
#求阶乘6！ =1*2*3*4*5*6
def jecheng(x):
    i = 1
    if x < 0:
        print ('负数没有阶乘')
    elif x == 0:
        return 1
    else:
        for n in range(1,x + 1):
            i = i * n
        return i
print jecheng(6)

#判断一个数是不是素数（除了1和他本身可以被整数）
def shushu(x):
    for n in range(2,x):
        if x % n == 0:
            print '不是素数'
            break  #如果循环·没有被break就执行else
    else:
        print '是素数'
shushu(8)
#函数的可变参数，一个*收集所有的未知参数
def lisi(*arg):
    print arg
lisi(4,5)
def lizi(**kwargs):
    print kwargs
lizi(xiaoming='shanghai',xiaoli='shenzhen')
#闭包：由函数动态生成的函数
def mi_num(x):    #输出一个函数
    def mi(y):
        y = y ** x
        return y
    return mi       #函数以参数的形式返回
a = mi_num(3)  #求三次方的函数
print a(2)   #2的3次
#lambda匿名函数
q = lambda x:x * x + 1
print q(2)


def fun1(a):
    a = a + 1
    print 'a=' + `a`
    return 0
k = 10
print "Before k=" + `k`
fun1(k)
print "After k = " + `k`
