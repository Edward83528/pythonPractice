# -*- coding: utf-8 -*-
"""
Created on Sat May 18 19:35:53 2019

@author: User
"""
import json;
import requests;

def getOpenData(url):
    return json.loads(requests.get(url).text);
def Dateformat(str):
    return str[0:4]+"-"+ str[4:6]+"-"+ str[6:8];