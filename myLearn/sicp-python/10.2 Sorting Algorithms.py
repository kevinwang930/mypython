# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 15:48:59 2018

@author: kevin
"""
import operator
import string

def selSort(L):
    suffixStart = 0
    while suffixStart != len(L):
        for i in range(suffixStart,len(L)):
            if L[i] < L[suffixStart]:
                L[suffixStart],L[i] = L[i],L[suffixStart]
        suffixStart += 1

def merge(left,right,compare):
    """Assumes left and right are sorted lists and
        compare defines an ordering on the elements.
       Returns a new sorted list containing both the 
        elements of left and right."""
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if compare(left[i],right[j]):
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j+=1
    while (i <len(left)):
        result.append(left[i])
        i +=1
    while (j < len(right)):
        result.append(right[j])
        j+=1
    return result

def mergeSort(L,compare = operator.lt):
    """Assumes L is a list, returns a new sorted list
        containing the same elements as L"""
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = mergeSort(L[:middle],compare)
        right = mergeSort(L[middle:],compare)
        return merge(left,right,compare)

#print(mergeSort([1,5,2,0,4,3,7,123,3434,121,143,26]))

def lastNameFirstName(name1,name2):
    name1 = name1.split(' ')
    name2 = name2.split(' ')
    if name1[1] !=name2[1]:
        return name1[1] < name2[1]
    else:
        return name1[0] < name2[0]
    
def firstNameLastName(name1,name2):
    name1 = name1.split(' ')
    name2 = name2.split(' ')
    if name1[0] != name2[0]:
        return name1[0] < name2[0]
    else:
        return name1[1] < name2[1]
    
L = ['Chris Terman','Tom Brady','Eric Grimson','Gisele Bundchen']
newL = mergeSort(L,lastNameFirstName)
print('Sorted by last name = ',newL)
newL = mergeSort(L,firstNameLastName)
print('Sorted by first name =',newL)


