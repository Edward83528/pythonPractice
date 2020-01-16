# -*- coding: utf-8 -*-
"""
Created on 2019/5/7

NCHU homework 20190504
Q5. 輸入三個整數x, y, z，請把這三個數由小到大輸出。

@author: Ginni Huang
"""


str = input("輸入三個整數，以空白分隔：")

str_list = str.split(" ")

try:
    if len(str_list) != 3:
        print("輸入錯誤")
    else:
        num_list = list(map(int, str_list))
        #print(str_list, num_list)
        
        num_list.sort()
        #print(num_list)
        for x in num_list:
            print(x)
    
except Exception:
    print("輸入錯誤")
    