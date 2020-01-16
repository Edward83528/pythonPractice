# -*- coding: utf-8 -*-
"""
串列(無形態之分,什麼都可以放)
list=[89,60,10]
list2=["Apple","pig"]
list3=[89,"sister"]

len():取長度
陣列.appand(值):串接
陣列.insert(插入處,值):插入
陣列.remove(值):移除
陣列.count(值):找數量,沒有為0
陣列.index(值):找索引值
陣列.extend(陣列):陣列如果放入另一個陣列元素
陣列[-1]:陣列最後一個元素值
陣列[start:end-1]:取陣列區段值

import使用:
import copy;
copy.copy(元素);

排序:    
值.sort();
reverse=True(從大排到小)
sorted(值,reverse=布林);
反轉:
值.reverse();

找最大值:
max(值);  
找最小值:
min(值);
"""
list0=[89,60,10,3,1,6,9,3,1,0,6,4]
list2=["Apple","pig"]
list3=[89,"sister"]
#python可從-1 -2 ...從後面開始抓
print(list0[-1]);
#python可從任一位置抓
print(list0[2:5]);
#python可從任一位置抓(再搭配for)
for s in list0[2:5]:
    print(s);
print("-"*30);
#===========================
for i in range(2):
    print(list3[i]);
print("-"*30);
#===========================
for i in range(len(list3)):
    print(list3[i]);
print("-"*30);
#===========================
for array in list3:
    print(array);
print("-"*30);
#===========================
#改變值
list0[2]="mom";
print(list0[2]);
print("-"*30);
#===========================
#append直接放在陣列後
list0.append("奇異果");
for array in list0:
    print(array);
print("-"*30);
#===========================
#insert插在陣列中
list0.insert(4,"草莓");
for array in list0:
    print(array);
print("-"*30);
#remove移除原素
list0.remove("奇異果");
for array in list0:
    print(array);
print("-"*30);
#===========================
#算出班級平均
scores=[]
total=inputscores=0;
while inputscores!=-1:
    inputscores=(int)(input("請輸入成績"));
    scores.append(inputscores);
    total+=inputscores;
print("平均分數為%d"%(total/(len(scores)-1)));
print("-"*30);
#===========================
#找數量
names=["cat","dog","pig","pig"];
print("豬有%d隻"%(names.count("pig")));
#找索引
name=["cat","dog","pig"];
if name.count("pig")>0:
    print(name.index("pig"));
print("-"*30);
#===========================
#刪除
zoos1=["dog","cat","bird","fish"];
zoos2=["mom","father"];
zoos1.extend(zoos2);
print(zoos1);
print("-"*30);
#===========================
#刪除
zoo=["dog","cat","bird","fish"];
data=input("請輸入你想移除的動物:");
if zoo.count(data)>0:
#if data in zoo:
    zoo.remove(data);
else:
    print("您輸入的動物不存在");
for mzoo in zoo:
    print(mzoo);
print("-"*30);
#import使用與複製陣列==========================
import copy;
copy1=[89,60,10,3,1];
copy2=copy1;
copy1[0]=20;
print("更改陣列某元素",copy2);
copy3=copy.copy(copy1);
copy3.append(200);
print("複製",list(copy3));
copy4=copy.deepcopy(copy1);
copy1.append(300);
print("深層複製",list(copy4));
print("-"*30);
#===========================
#import使用與複製陣列==========================
scorses=[1,4,3,1,9,6,8];
#從小排到大
scorses.sort();
print(scorses);
#反轉
scorses.reverse();
print(scorses);
scorses2=sorted(scorses,reverse=True);
print("從大排到小",scorses2);
print("最大",max(scorses));
print("最大",min(scorses));
print("-"*30);
#===========================

