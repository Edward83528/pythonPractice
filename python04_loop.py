# -*- coding: utf-8 -*-
"""
數列:
1.range(end-1)
ex:range(10) =>0~9

2.range(start,end-1)  
ex: range(1,10) =>1~9

3.range(start,end-1,step)
ex: range(1,10,2) =>1 3 5 7 9
ex:range(10,1,-1) =>10 9 8 7 6 5 4 3 2

迴圈:
    1.for迴圈
    2.while迴圈
for 變數名 in 數列:
    要跑的程式;
    
for 變數名 in 數列:
    for 變數名2 in 數列:
    要跑的程式;    
    
格式化:
print("項目數"%(項目值));
(印出1乘100文字):
print("%d x %d" %(1,100));
%d整數
%s字串
%f浮點數
%e科學符號
%5d,至少長度為5,不足補空白
"""
scors=95;
name="Harry";
rate=0.27
print("姓名:%s的分數為%d"%(name,scors));
print("利率為%.2f"%(rate));
print("姓名:%s的分數為%5d"%(name,scors));
print("-"*30);
#===================================
r1=range(10);     
r2=range(1,10);   
r3=range(1,10,2);
r4=range(10,1,-1); 
#list相當於陣列
print(list(r1));
print(list(r2));
print(list(r3));
print(list(r4));
print("-"*30);
#===================================
for i in range(10):
    print(i,end='',sep=',');
print();
print("-"*30);
#===================================
for i in range(10,4,-1):
    print(i,end='',sep=',');
print();
print("-"*30);
#===================================
for x in range(1,10):
    for y in range(1,10):
        print("%dx%d=%d\t" %(x,y,x*y),end="");
    print();
print();
print("-"*30);
#印出巴斯卡三角形===================================
for i in range(1,6):
    print();
    for x in range(1,i+1):
        print(i,end="");
print();
print("-"*30);
#印出字串中有幾個特定字母===================================
word="this is book";
count=0;
for i in word:
    if word=='o':
        count+=1;
print("b的字母有%d個" %(count));
print("-"*30);
#while=======================
i=1;
while i<10:
    print(i);
    i+=1;
print();
print("-"*30);
#while階層數=======================
totals=i=1;
n=(int)(input('請輸入階層數'));
while i<=n:
    totals*=i;
    print(i);
    i+=1;
print("%d階的和為%d" %(n,totals));
print();
print("-"*30);
#猜數字=======================
answer=31;
guess=0;
while answer!=guess:
    guess=(int)(input('請輸入1~100的數'));
    if guess<31:
        print("太小嚕");
    elif guess>31:
        print("太大了");
    else:
        print("答對嚕");
        break;
print();
print("-"*30);
#continue break=======================
while True:
    fruit=(input('請輸入喜歡的水果,q離開'));
    if fruit=='q':
        break;
    print("你喜歡的水果為",fruit);
print("已離開");
print();
print("-"*30);
#最小公倍數=======================
a=(int)(input('請輸入第一個數'));
b=(int)(input('請輸入第二個數'));
max=(a+1)*(b+1);
for i in range(1,max):
    if i%a==0 and i%b==0:
        print("最小公倍數為:",i);
        break;
print();
print("-"*30);
#找質數=======================
start=(int)(input('請輸入第一個數'));
end=(int)(input('請輸入第二個數'));
check=True;
for i in range(start,end):
    for j in range(2,i):
        if i%j==0:
            check=False;
        if check==True:
            print(i,end=',');
print();
print("-"*30);
#1~number基數的總合=======================
number=(int)(input('inpute number(1~number奇數的總合):'))
for i in range(1,number+1):
    if(i%2==1):
        number+=i;
        print(i,end=',');
print("SUM2:",number);
print("-"*30);
