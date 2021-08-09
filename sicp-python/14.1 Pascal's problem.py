# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 15:20:14 2018

@author: kevin
"""
import random

def rollDie():
    return random.choice([1,2,3,4,5,6])

def checkPascal(numTrials):
    numWins = 0.0
    for i in range(numTrials):
        for j in range(24):
            d1 = rollDie()
            d2 = rollDie()
            if d1 == 6 and d2 == 6:
                numWins +=1
                break
    print('Probability of winning =', numWins/numTrials)
    
checkPascal(1000000)