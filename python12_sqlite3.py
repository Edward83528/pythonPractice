# -*- coding: utf-8 -*-
"""
sqlite3使用
"""
import sqlite3
#連接db(不存在自動創建)
conn=sqlite3.connect('test.db');
#sql字串
sql_create="create  table member(id integer primary key autoincrement not null,name text,age int,address varchar(200));";
sql_insert="insert into member(name,age,address) values('Tom',18,'this');"
sql_inserts="insert into member(name,age,address) values('Tom',18,'this'),('Tom2',18,'this'),('Tom3',18,'this');"
sql_select="select * from member";
sql_update="update  member set address='台灣大道' where id=2";
sql_delete="delete from member where id=1";
#執行sql 
#新增資料表==========
#conn.execute(sql_create);
#新增資料===========
#conn.execute(sql_insert);
#conn.commit();
#print("資料新增成功");
#查詢資料============
cursor=conn.execute(sql_select);
for row in cursor:
    print("ID:",row[0]);
    print("name:",row[1]);
    print("age:",row[2]);
    print("address:",row[3]);
conn.close;
#修改資料===========
#conn.execute(sql_update);
#conn.commit();
#print("資料修改成功");
#刪除資料===========
#conn.execute(sql_delete);
#conn.commit();
#print("資料刪除成功");



