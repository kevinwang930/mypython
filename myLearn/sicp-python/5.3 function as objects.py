# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 22:36:01 2018

@author: kevin
"""

def applyToEach(L,f):
    """Assume L is a list, f a function
       Mutates L by replacing each elment e in L by f(e) """
    for i in range(len(L)):
        L[i]= f(L[i])
        
L =[1,-2,3.33]
print('L=',L)
applyToEach(L,abs)
print('L=', L)

str = 'abc'
str1 = str.replace('b','d')
print(str1)

