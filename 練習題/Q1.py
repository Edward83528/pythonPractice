# -*- coding: utf-8 -*-
"""
Created on 2019/5/4

NCHU homework 20190504
Q1. 有四個數字：1, 2, 3, 4，能組成多少個互不相同且無重複數的三位數？各是多少？

@author: Ginni Huang
"""

list = [1,2,3,4]

cnt = 0
for i in list:
    for j in list:
        for k in list:
            if i != j and j != k and k != i:
                print(i,j,k, sep="")
                cnt += 1
                
print("*" * 30)
print("以上，共%d個" % cnt)