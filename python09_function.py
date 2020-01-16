# -*- coding: utf-8 -*-
"""
def 函式名稱(參數名稱):
    程式區塊;
    return 值;

要給它隻程式的話,主程式要加上
if __name__=='__main__':
    主程式;

變數加上global變全域變數 

format的使用:
"總和:{:,}".format(值);

"""
#=================================== 
#全域變數
num=10;
def calArea(h,w):
    return h*w;
def calTemperature(c):
    return c*1.8+32;
def showNumber():
    #區域變數
    #global num;#加上global變全域變數
    num=5;
    print(num);
def total(num1,num2,num3):
    result=0;
    for i in range(num1,num2,num3):
        result+=i;
    return result;
#可以指定預設值===================
def person(name,school='興大'):
    print("姓名:"+name);
    print("學校:"+school);

def addnumber(x,y=[]):
    y.append(x);
    print(y);
#長度不一時===================
def calclu(*value):
    result=1;
    for i in value:
        result+=i;
    return result;
#===================================       
if __name__=='__main__':

    print("面積:",calArea(3,5));
    print("number:",showNumber());
    print("分辨全域區域/變數:",num);

    print("="*30);
#計算總合===========================
    key=input("按Y開始");
    while key=='Y':
        start=(int)(input("輸入初始值"));
        end=(int)(input("輸入終止值"));
        step=(int)(input("輸入間隔值"));
        print("總和:{:,}".format(total(start,end,step)));
        key=input("按Y繼續,其他離開");
    print("="*30);

#可以指定預設值===================
    print(person("harry"));
    print(person("tom","清大"));
    print(addnumber(10,[1,2,3]));
    print(addnumber(20,[10,20]));
    print(addnumber(30));
#值不固定=============
    print(calclu());
    print(calclu(5,3,2,1));
    print(calclu(10,100));
    
