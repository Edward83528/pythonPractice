# -*- coding: utf-8 -*-
"""
Created on 2019/5/7

NCHU homework 20190504
Q4. 輸入某年某月某日，判斷這一天是這一年的第幾天？

@author: Ginni Huang
"""
import datetime

#dt = datetime.datetime.strptime("2017/1/1","%Y/%m/%d")
#week = dt.strftime("%j")
#print(week)

def validate(date_text):
    try:
        dt = datetime.datetime.strptime(date_text, '%Y/%m/%d')
        return [True, dt]
    except ValueError:
        return [False, None]


while True:
    date_text = input("請輸入日期(格式=yyyy/m/d)：")
    
    res = validate(date_text)
    if res[0]:
        dt = res[1]
        print("%s 為這一年的第 %s 天" % (date_text, dt.strftime("%j")))
        
    else:
        if date_text == "":
            break
        else:
            print("日期格是錯誤，請重新輸入！")