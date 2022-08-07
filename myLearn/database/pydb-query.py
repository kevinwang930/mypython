# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:59:29 2020

@author: kevin
"""


from __future__ import print_function
from datetime import date, datetime, timedelta
from db import mydb,mycursor

c = mycursor.execute('show databases;')
for x in c:
    print(x)