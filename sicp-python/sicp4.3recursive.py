# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 16:10:35 2018

@author: kevin
"""
#m = 0
def fib(n):
    """Assume n an int >0
        returns fibonacci of n"""
    #if n==2:
        #m = m+1
    if n ==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    

    
    
def testFib(n):
    for i in range(n+1):
        print('fib of ',i,'= ',fib(i))

def isPalindrome(s):
    """Assumes s is a str
       Returns True if the letters in s form a palindrome;
        False otherwise. Non-letters and Capitalization are ignored."""
    def toChars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters
    def isPal(s):
        print('isPal called with',s)
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(toChars(s))

def testIspalindrome():
    print('try dogGod')
    print(isPalindrome('dogGod'))
    print('try doGood')
    print(isPalindrome('doGood'))


    
        
