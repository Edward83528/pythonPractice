# -*- coding: utf-8 -*-
"""
Created on Sat May 18 21:17:16 2019

@author: User
"""
import sqlite3
#連接db(不存在自動創建)===============
conn=sqlite3.connect('OpenData.db');
#SQL字串==========================
sql_selectBike="select station,space,rent,id from Bike ";
#使用者查詢===========================
print("此系統為新北市與台南市公共自行車租用查詢系統");
city=(input('請輸入您想查詢的城市(欲查詢新北市請按A,查詢台南市請按B):'));
#====================================
stationName=(input('請輸入您想查詢的站名:'));
if city=='A' or city=='a':
    #查詢自行車資料========================
    cursor=conn.execute(sql_selectBike+" where category='A' and station like '%"+stationName+"%' order by id  ");
    print("以下為符合您所輸入的查詢資訊");
    for row in cursor:
        print("%s:有%d台公用腳踏車可租借且還有%d台歸還空位" %(row[0],row[1],row[2]));
        print("=:"*30);
    conn.close;
elif city=='B' or city=='b':
    cursor=conn.execute(sql_selectBike+" where category='B' and station like '%"+stationName+"%' order by id ");
    for row in cursor:
       print("%s:有%d台公用腳踏車可租借且還有%d台歸還空位" %(row[0],row[1],row[2]));
       print("=:"*30);
    conn.close;