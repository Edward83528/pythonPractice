# -*- coding: utf-8 -*-
"""
判斷式有三種(注意是用縮排判斷區塊):
1.
if(條件式boolean):
    成立時才做
2.
if(條件式boolean):
    True做的事
else:
    False做的事
3.
if(條件式boolean):
    True做的事
elif(條件式boolean):
    True做的事
elif(條件式boolean):
    True做的事
else:
    False做的事
"""
#month=1;
#可以用input()做輸入(預設是字串型態)
month=int(input("請輸入月份:"))
#if(month==1 or 3 or 5 or 7 or 8 or 10 or 12): #可以用這樣的方式簡化句子
if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
    print("這個月有31天");
elif(month==2):
    print("這個月有28天");
else:
    print("這個月有30天");
    
