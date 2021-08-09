# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 15:00:47 2018

@author: kevin
"""

#Newton-Raphson for square root
#Find x such that x**2 - 24 is within epsilon of 0.01
epsilon = 0.01
k = 985
guess = k/2.0
i = 0
while abs(guess*guess-k) >=epsilon:
    guess = guess-(guess*guess - k)/(2*guess)
    i=i+1
    print(i,'th guess is ',guess)
print('Square root of ',k,' is about',guess)



#bisection search
numGuess = 0
lowGuess = 0
highGuess = max(1.0,k)
ans = (highGuess + lowGuess)/2.0
while abs(ans**2 -k) >= epsilon:
    numGuess = numGuess + 1
    if ans**2 <k:
        lowGuess = ans
    else:
        highGuess = ans
    ans = (highGuess + lowGuess)/2.0
    print(numGuess,'th guess is ',ans)
print('Square root of ',k,' is about',ans)
