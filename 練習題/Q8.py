# -*- coding: utf-8 -*-
"""
Created on 2019/5/8

NCHU homework 20190504
Q8. 印出9x9乘法表

@author: Ginni Huang
"""


print("\n九九乘法表\n")



for i in range(1, 10):
    
    
    for j in range(2, 6):
        
        print("%d X %d = %d" % (j, i, i*j), end="\t")
        
    print()
    
        
print()
print("*" * 60)

for i in range(1, 10):
    
    
    for j in range(6, 10):
        
        print("%d X %d = %d" % (j, i, i*j), end="\t")
    
    print()
    
    