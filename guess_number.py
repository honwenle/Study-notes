#! /usr/bin/env python
#coding:UTF-8

import random

x = random.randint(0,100)

while True:
    gx = raw_input('Please input a number(0~100):')
    if not gx.isdigit():
        print u'请输入数字'
    elif int(gx) > 100 or int(gx) < 0:
        print u'请输入0到10之间的数字'
    else:
        if int(gx) == x:
            print u'恭喜，猜中了'
            break
        elif int(gx) > x:
            print u'高了'
        else:
            print u'低了'
