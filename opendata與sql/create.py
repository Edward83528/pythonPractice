# -*- coding: utf-8 -*-
"""
Created on Sat May 18 19:57:58 2019

@author: User
"""
import sqlite3
#連接db(不存在自動創建)===========================
conn=sqlite3.connect('OpenData.db');
#SQL字串=========================================
sql_createCity='''create  table if not exists City(
id integer primary key autoincrement not null,
name varchar(10),
sequence int
);''';
sql_createBike='''create  table if not exists Bike(
id integer primary key autoincrement not null,
category varchar(1),
station varchar(50),
space int,
rent int,
Latitude varchar(50),
Longitude varchar(50),
UpdateTime varchar(50)
);''';
#新增資料表======================================
conn.execute(sql_createCity);
conn.execute(sql_createBike);
print("資料表新增成功");
conn.close;
#================================================
