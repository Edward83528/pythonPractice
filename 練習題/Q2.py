# -*- coding: utf-8 -*-
"""
Created on 2019/5/5

NCHU homework 20190504
Q2. 企業發放的獎金根據利潤提成。 利潤(I)低於或等於10萬元時，獎金可提10%；
利潤高於10萬元，低於20萬元時，低於10萬元的部分按10%提成，高於10萬元的部分，可提成7.5%；
20萬到40萬之間時，高於20萬元的部分，可提成5%；40萬元到60萬元之間時，高於40萬元的部分，可提成3%；
60萬到100萬之間時，高於60萬元的部分，可提成1.5%；
高於100萬元時，超過100萬元的部分按1%提成，從鍵盤輸入當月利潤，求應發放獎金總數？

@author: Ginni Huang
"""


I = int(input("請輸入當月利潤(單位=萬元)："))

tmp_i = I

bonus = 0


if tmp_i > 100:
    caled = tmp_i - 100
    bonus += caled * 0.01
    tmp_i -= caled
    
if tmp_i > 60:
    caled = tmp_i - 60
    bonus += caled * 0.015
    tmp_i -= caled
    
if tmp_i > 40:
    caled = tmp_i - 40
    bonus += caled * 0.03
    tmp_i -= caled    
    
if tmp_i > 20:
    caled = tmp_i - 20
    bonus += caled * 0.05
    tmp_i -= caled
    
if tmp_i > 10:
    caled = tmp_i - 10
    bonus += caled * 0.075
    tmp_i -= caled
    
if tmp_i > 0:
    caled = tmp_i
    bonus += caled * 0.1
    

print("本月獎金 = %.2f (萬元)" % bonus)


