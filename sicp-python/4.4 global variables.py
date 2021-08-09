# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 20:43:11 2018

@author: kevin
"""

def fib(n):
    """Assume n an int >0
        returns fibonacci of n"""
    #if n==2:
        #m = m+1
    global numFibcalls
    numFibcalls +=1
    if n ==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    

    
    
def testFib(n):
    for i in range(n+1):
        global numFibcalls
        numFibcalls = 0
        print('fib of ',i,'= ',fib(i))
        print('fib called ',numFibcalls,' times')