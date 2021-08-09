# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 21:41:23 2018

@author: kevin
"""

nameHandle = open('kids','a')
for i in range(2):
    name = input('Enter name: ')
    nameHandle.write(name + '\n')
nameHandle.close()

nameHandle = open('kids','r')
for line in nameHandle:
    print (line)   
nameHandle.close()