# -*- coding: utf-8 -*-
"""
解析json

import json;
"""
import json;
import requests;
url="http://tbike.tainan.gov.tw:8081/Service/StationStatus/Json";
response=json.loads(requests.get(url).text);
print(response);
StationNam=[];
for data in response:
    StationNam.append(data["StationName"]);
for i in range(len(StationNam)):
    print(StationNam[i]);