# -*- coding: utf-8 -*-
# @Time    : Created on 2017/8/31 19:52
# @Author  : JiaHong
from python02_s import *
print "This program will calculate the area of triangle."
a = 0
b = 0.0
h = 0
area1 = 0.0
a = input("Please input a -- >")
h = input("Please input h -- >")
b = input("Please input b -- >")
area1 = calcu_tri(a,h)
print "三角形的面积是 " + `area1`
area2 = calcu_zhengf(b)
print "正方形的面积是"  + `area2`
