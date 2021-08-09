# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 15:21:06 2018

@author: kevin
"""

def search(L,e):
    for i in range(len(L)):
        if L[i] ==e:
            return True
    return False

def searchAscending(L,e):
    """Assumes L is a list, the elements of which are in
        ascending order.
       Returns True if e is in L and False otherwise"""
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def searchBinary(L,e):
    def bSearch(L,e,low,high):
        if high == low:
            return L[low] == e
        mid = (low+high)/2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:
                return False
            else:
                return bSearch(L,e,mid+1,high)
    
    if len(L) == 0:
        return False
    else:
        return bSearch(L,e,0,len(L)-1)
            