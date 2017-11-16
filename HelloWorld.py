# -*- coding: utf-8 -*- 这行代码的含义是本文件使用utf-8编码（可以使用中文），否则就是assic编码了
# 2007-8-27
print "This program will calculate the area of triangle."
a = 0
h = 0
area = 0.0
a = input("Please input a-->") #使用input 输入，input是一个函数
h = input("Please input b-->")
# print a
# print h
area = 1.0 * a * h / 2
print "Area is " + `area` #利用一组反引号，将数字转化成为字符创`
print "面积是" + str(area) #利用str函数将数字转化成为字符串

print "This program will calculate the area of trapezoid."
a1 = 0
a2 = 0
hh = 0
area2 = 0.0
a1 = input("Please input a1-->")
a2 = input("Please input a2-->")
hh = input("Please input hh-->")
area2 = 1.0 * (a1 + a2) * hh / 2
print "This area2 is " + `area2`

PI = 3.1415
r = 0
area3 = 0.0
r = input("请输入圆的半径r-->")
area3 = PI * r * r
print "圆的面积是" + `area3`



