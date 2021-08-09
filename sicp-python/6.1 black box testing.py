# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 14:00:35 2018

@author: kevin
"""

def copy(L1,L2):
    """Assume L1, L2 are lists,
       Mutates L2 to be a cope of L1"""
    while len(L2) > 0:
        L2.pop()
    for e in L1:
        L2.append(e)
    print(L2)
    
L = [1,2,3]
L1 = L
L2 = L

copy(L1,L2)
