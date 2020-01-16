# -*- coding: utf-8 -*-
"""
Created on 2019/5/8

NCHU homework 20190504
Q6. 印出費氏數列(Fibonacci sequence)，又稱黃金分割數列，指的是這樣的一個數列：0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ....

@author: Ginni Huang
"""

def FIB(n):
    if n == 0 or n == 1:
        return n
    else:
        return FIB(n-1) + FIB(n-2)
    

try:
    
    ubound = int(input("請輸入費氏數列長度："))

    for i in range(0, ubound):
        print(FIB(i))

except Exception:
    print("輸入錯誤")