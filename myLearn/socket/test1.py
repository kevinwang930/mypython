# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 14:00:42 2020

@author: kevin
"""

import sys
host = sys.argv[1]
print(host)

class Warehouse:
        purpose = 'storage'
        region = ['west']

w1=Warehouse()
w2=Warehouse()
print(w1.region)
w2.region[0] = 'east'
print(w1.region)
