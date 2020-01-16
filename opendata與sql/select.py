# -*- coding: utf-8 -*-
"""
Created on Sat May 18 20:16:04 2019

@author: User
"""
import sqlite3
#連接db(不存在自動創建)===============
conn=sqlite3.connect('OpenData.db');
#SQL字串==========================
sql_selectCity="select * from City";
sql_selectBike="select * from Bike";
#查詢城市資料============
cursor=conn.execute(sql_selectCity);
for row in cursor:
    print("id:",row[0]);
    print("name:",row[1]);
    print("sequence:",row[2]);
conn.close;
#查詢自行車資料========================
cursor=conn.execute(sql_selectBike);
for row in cursor:
    print("id:",row[0]);
    print("category:",row[1]);
    print("station:",row[2]);
    print("space:",row[3]);
    print("rent:",row[4]);
    print("Latitude:",row[5]);
    print("Longitude:",row[6]);
    print("UpdateTime:",row[7]);
conn.close;
#====================================