# -*- coding: utf-8 -*-
"""
Created on Sat May 18 20:25:23 2019

@author: User
"""
import sqlite3
#連接db(不存在自動創建)==============
conn=sqlite3.connect('OpenData.db');
#SQL字串============================
sql_deleteCity="drop table City";
sql_deleteBike="drop table Bike";
#刪除資料===========================
conn.execute(sql_deleteCity);
conn.execute(sql_deleteBike);
conn.commit();
print("資料表刪除成功");
conn.close;
#===================================