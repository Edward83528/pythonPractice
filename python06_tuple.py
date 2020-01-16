# -*- coding: utf-8 -*-
"""
元組(不能被修改的陣列)
"""

tuple1=(10,20,30,40);
print(tuple1[0]);
#元組不能被修改(TypeError: 'type' object does not support item assignment)
#tuple[0]=900;
#但指定到list可修改,修改完再指定回來
list1=list(tuple1);
list1[0]=300;
tuple1=tuple(list1);
print(tuple1);