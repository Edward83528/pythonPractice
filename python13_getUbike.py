# -*- coding: utf-8 -*-
"""
得到open data Ubike資料存到sqlite3
"""
import json;
import requests;
import sqlite3
#讀取opendata ubike資料======================
url="http://data.ntpc.gov.tw/od/data/api/54DDDC93-589C-4858-9C95-18B2046CC1FC?$format=json";
response=json.loads(requests.get(url).text);
#print(response);
#連接db(不存在自動創建)========================
conn=sqlite3.connect('openData.db');
#sql字串======================================
sql_create='''
create  table if not exists ubike(
id integer primary key autoincrement not null,
station varchar(50),
space int,
rent int);''';
sql_select="select * from ubike";
#新增資料表====================
conn.execute(sql_create);
'''
#跑迴圈新增資料================
for row in response:
    conn.execute("insert into ubike(station,space,rent)values('%s',%d,%d)"%(row['sna'],int(row['bemp']),int(row['sbi'])));
conn.commit();
'''
#查詢ubike資料============
cursor=conn.execute(sql_select);
for row in cursor:
    print("ID:",row[0]);
    print("station:",row[1]);
    print("space:",row[2]);
    print("rent:",row[3]);
conn.close;