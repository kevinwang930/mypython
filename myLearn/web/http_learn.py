# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 11:40:12 2019

@author: kevin
"""
import requests
r = requests.get('https://www.baidu.com')
print(r.status_code)
print(r.headers)
