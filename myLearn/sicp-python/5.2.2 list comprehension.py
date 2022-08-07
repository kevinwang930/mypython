# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 22:24:50 2018

@author: kevin
"""

L = [x**2 for x in range(1,7)]
print(L)
mixed = [1,2,'a',3,4.0]
print([x**2 for x in mixed if type(x) == int])