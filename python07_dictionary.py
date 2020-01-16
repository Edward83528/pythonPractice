# -*- coding: utf-8 -*-
"""
字典
變數={key:value,key:value,......}

1.key值如果重複會抓出最後一個
    set(字典)會自動過濾重複值
2.如果輸入沒有的key值,會發生錯誤
    用 字典.get(key),找不到會出現None(預設值)
       字典.get(key,"自訂值")  
"""

#基本
dist1={"name":"小明","錢":300}
print(dist1);
print(dist1["錢"]);
#KeyError: 'e'
#print(dist1["e"]);
print(dist1.get("e"));
print(dist1.get("e","無key"));
print("="*30);
#Key取出value=========================
content={
        "A":"內向",
        "B":"外向",
        "O":"聰明"
        };
blood=input("請輸入您的血型");
result=content.get(blood);
if(result!=None):
    print(result);
else:
    print("找不到血型");
#更改value=========================
content2={
        "A":"內向",
        "B":"外向",
        "O":"聰明"
        } ;
#修改某值
content2["A"]="瘋狂";
#修改某值,如果沒key值就會新增
content2["AB"]="害羞";
print(content2);
#刪除某值
del content2["A"];
#刪除變數
#del content2;
print(content2);
#清空
#content2.clear();
print(content2);
#找Key是否在字典裡
print("A" in content2);
print("B" in content2);
print("="*30);

#輸入並查詢學生成績========
student={
        "張1":90,
        "張2":95,
        "張3":80
        } ;
name=input("請輸入學生姓名:");
if(name in student ):
    print(student.get(name));
else:
    #記得觀察value型態適時轉型
    scores=(int)(input("請輸入分數:"));
    student[name]=scores;
    print(student);

#顯示字典所有元素============
datas={
        "a":2,
        "b":5,
        "c":9
        } ;
key=datas.keys();
value=datas.values();
#轉成list
keylist=list(key);
valuelist=list(value);
#迴圈印出
for i in range(len(keylist)):
    print(keylist[i],valuelist[i]);
print("="*30);
#列出所有的item功能(會為一個二維值)
print(datas.items());
print(list(datas.items()));#[('a', 2), ('b', 5), ('c', 9)]
print(list(datas.items())[0][1]);

#item搭配in===========
datas1={
        "z":6,
        "x":7,
        "v":8
        };
for v in datas1.values():
    print("value:",v);
print("="*30);
#for用兩個參數
for k,v in datas1.items():
    print(k,v);
print("="*30);

