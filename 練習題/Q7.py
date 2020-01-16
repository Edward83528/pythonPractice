# -*- coding: utf-8 -*-
"""
Created on 2019/5/8

NCHU homework 20190504
Q7. 將一個列表的數據複製到另一個列表中

@author: Ginni Huang
"""

import copy


animals = ["台灣黑熊", ["石虎", "雲豹"], "水鹿", "山羌", "黃喉貂"]

copy_animals = copy.copy(animals)
deepcopy_animals = copy.deepcopy(animals)

print("animals=", animals)
print("copy_animals=", copy_animals)
print("deepcopy_animals=", deepcopy_animals)

print("*"*30)


animals[2] = "梅花鹿"
animals[1][1] = "X"

print("animals=", animals)
print("copy_animals=", copy_animals)
print("deepcopy_animals=", deepcopy_animals)


