# -*- coding: utf-8 -*-
"""
Created on 2019/5/5

NCHU homework 20190504
Q3. 一個整數，它加上100後是一個完全平方數，再加上168又是一個完全平方數，請問該數是多少？

@author: Ginni Hunag
"""

import math

#驗證是否完全平方數
def is_sqr(n):
    a = int(math.sqrt(n))
    return a * a == n

lbound = 100 + 168
for i in range(lbound, 10000, 1):
    
    res1 = is_sqr(i + 100)
    res2 = is_sqr(i + lbound)
    #print(i, res1, res2)
    if res1 and res2:
        
        print("ans =", i)
        break
    
    