# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 22:02:25 2018

@author: kevin
"""

t1= ()
t2=(1,'kevin',3)
s1 = 'kevin'
t3=(t2,3.14)

print(t1)
print(t2)
print(t1+t2)
print(t3)
print((t1+t2)[2])
print(((t1+t2)[1])[2:4])
print(((t1+t2)[1])[2:5])
print(((t1+t2)[1])[4])
print(((t1+t2)[1])[2:])

def findDivisors(n1,n2):
    """Assume that n1 and n2 are positive ints, 
       Returns a tuple containing all common divisors of n1 & n2"""
    divisors = () #empty tuple
    for i in range(1,min(n1,n2)+1):
        if n1%i==0 and n2%i == 0:
            divisors = divisors + (i,)
    return divisors

divisors = findDivisors(20,100)
print(divisors)
total = 0
for d in divisors:
    total += d
print(total)

def findExtremeDivisors(n1,n2):
    """Assumes that n1 and n2 are positive ints,
        Returns a tuple containing the smallest common
        Divisor>1 and the largest common divisor of n1 
        ad n2"""
    divisors = ()
    minVal,maxVal = None,None
    for i in range(2, min(n1,n2)+ 1):
        if n1%i == 0 and n2%i == 0:
            divisors = divisors + (i,)
            if minVal == None or i < minVal:
                minVal = i
            if maxVal == None or i > maxVal:
                maxVal = i
    return(minVal,maxVal,divisors)
    
minDivisor,maxDivisor,Divisors = findExtremeDivisors(100,200)
print(minDivisor,maxDivisor,Divisors)
