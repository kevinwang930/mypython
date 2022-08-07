# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 15:43:39 2018

@author: kevin
"""

def fib(n):
    '''Assumes n is an int >= 0
        Returns Fibonacci of n '''
    if n == 0 or n == 1:
        return 1
    else:
        print('fib',n-1,'+','fib',n-2)
        return fib(n-1)+fib(n-2)
    
def fastFib(n,memo = {}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        print('fib',n-1,'+','fib',n-2)
        result = fastFib(n-1,memo)+fastFib(n-2,memo)
        memo[n] = result
        return result
    
print(fastFib(120))