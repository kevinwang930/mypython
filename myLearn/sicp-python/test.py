# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 10:46:43 2018

@author: kevin
"""
import numpy

A = numpy.array([1,2,3])
B = numpy.array([4])
B = numpy.append(B,A)
print(B)
k = [1,2,3]
j = k
j[1] = 5
print(k)


#test arguments 

def passTest():
    A = [1,2,3]
    B = passA(A)
    print(A)
    
def passA(A):
    A.append(4)
    return A

passTest()