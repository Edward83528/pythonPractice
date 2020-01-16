# -*- coding: utf-8 -*-
"""
Created on Sat May 18 19:52:25 2019

@author: User
"""
import sqlite3
import function;
#連接db(不存在自動創建)
conn=sqlite3.connect('OpenData.db');
#OpenData URL==================================================================
bikeUrl_nptc="http://data.ntpc.gov.tw/od/data/api/54DDDC93-589C-4858-9C95-18B2046CC1FC?$format=json";
bikeUrl_tainan="http://tbike.tainan.gov.tw:8081/Service/StationStatus/Json";
#SQL字串=======================================================================
sql_insertCity="insert into City(name,sequence) values('新北市','A'),('台南市','B');"
#新增城市資料==================================================================
conn.execute(sql_insertCity);
conn.commit();
print("城市資料新增成功");
#跑迴圈新增自行車資料===========================================================
response_nptc=function.getOpenData(bikeUrl_nptc);
for row in response_nptc:
    conn.execute("insert into Bike(category,station,space,rent,Latitude,Longitude,UpdateTime)values('%s','%s',%d,%d,'%s','%s','%s')"%('A',row['sna'],int(row['bemp']),int(row['sbi']),(row['lat']),(row['lng']),(function.Dateformat(row['mday'][0:8]))));
conn.commit();
print("新北市自行車資料新增成功");
response_tainan=function.getOpenData(bikeUrl_tainan);
for row in response_tainan:
    conn.execute("insert into Bike(category,station,space,rent,Latitude,Longitude,UpdateTime)values('%s','%s',%d,%d,'%s','%s','%s')"%('B',row['StationName'],row['AvaliableSpaceCount'],row['AvaliableBikeCount'],(row['Latitude']),(row['Longitude']),(row['UpdateTime'][0:10])));
conn.commit();
print("台南市自行車資料新增成功");
conn.close;
#==============================================================================
