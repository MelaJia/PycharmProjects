# -*- coding: utf-8 -*-
print r'''静夜思
床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。'''
print abs(-8)    #此函数求绝对值
print cmp(1,2)     #cmp()函数将比较1和2,1<2，返回值为-1
print int('45')  #int()将字符串转化成整型
print str(45.2)   #str()函数将其他数据类型转换成字符串
l=['s']
print l
L = ['Adam', 'Lisa', 'Bart']
for name in L:
    print name
#while循环，求100以内的奇数和
x = 1
s = 0
while x < 100:
    s = s + x
    x = x + 2
print s

sum = 0
x = 1
while True:
    sum = sum + x
    x = 2 * x + 1
    if x > 100:
        break
print sum
d = {
    'a': 1,
    'b': 2,
    'c': 3
}
for key in d:
    print key + ":",d[key]
a = [12,13,16,9]
b = list('beijing')
print b
#print b[2:5]
print b[-1]  #切出最后一位,g
print b[-2: ]  #最后两位 ['n', 'g']
print b[ :2]   #切前面两位 ['b', 'e']
print b[::-1]  #倒序排列出来 ['g', 'n', 'i', 'j', 'i', 'e', 'b']
print b[1:6:2]  #从第1开始，每隔两位取出一位 ['e', 'j', 'n']
b[-3:] = list('abc')  #分段修改，改变最后三位 ['b', 'e', 'i', 'j', 'a', 'b', 'c']
print b
print b + a  #合并列表 ['b', 'e', 'i', 'j', 'a', 'b', 'c', 12, 13]
a.append(45)   #增加元素,[12, 13, 45]
print a
a.pop()   #默认删除最后一位，并且返回最后一位,[12, 13]
print a
a=[[1, 2, 3], 13, 16, 9]
print a
print a[0][1]

d = {
    'a': 1,
    'b': 2,
    'c': 3
}
print 'a' in d #判断a元素是否在字典里面，是返回true
print d.keys()  #读取d字典里面的所有元素
print d.values()  #读取d字典里面的所有元素值
print d.items()    #读取字典的所有简直对

m = [12,12,45,65,98,78]
c = set(m)
print c  #集合可以去掉重复的数字，set([65, 98, 12, 45, 78])
print 12 in c
#假设我们让用户输入星期一至星期日的某天，如何判断用户的输入是否是一个有效的星期呢？
weekdays = set(['Mon','Tue','Wed','Thur','Fri','Sat','Sun'])
x1 = 'Mo'
if x1 in weekdays:
    print 'input ok!'
else:
    print 'input error!'

s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
   # print x
    print x[0] + ': ',x[1]
   #Lisa:  85
#Adam:  95
#Bart:  59
print '姓名 ' + ' 年龄 ' + ' 籍贯 '
#set()集合里面传入列表list
cl = set([('张三','32','北京'),('李四','45','天津'),('王五','28','河北')])
for x in cl:
    print x[0] + '   ' + x[1] + '  ' + x[2]
#
# for x in cl:
#    for y in x:
#        print y



