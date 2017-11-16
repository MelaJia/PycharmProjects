# -*- coding: utf-8 -*-
# @Time    : Created on 2017/11/15 23:36
# @Author  : JiaHong
# 猜猜数字游戏
import random
# game_count记录共玩了几次
# all_count 记录每次玩的猜测数 list[]


game_count=0
all_count=[]
while True:
    guess_count = 0
    game_count+=1
    answer = random.randint(0, 99)
    while True:
        guess=input("请输入你要猜的数字:->")
        guess_count+=1
        if guess==answer:
             print "恭喜你，猜中了！"
             print "你总共猜了"+str(guess_count)+"次"
             all_count.append(guess_count)
             break
        elif guess > answer:
            print "你猜的数字大了！"
        else:
             print "你猜的数字小了！"
    onemore =raw_input("你还要再玩一次吗？(Y/N)")
    if onemore == 'N' or onemore == 'n':
        print "欢迎下次再来玩！"
        print "你的成绩如下："
        print all_count
        print "平均成绩"+str(sum(all_count)/float(len(all_count)))
        break




