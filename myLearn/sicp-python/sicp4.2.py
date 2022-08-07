# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 11:56:35 2018

@author: kevin
"""

def findRoot(x, power, epsilon):
    """Assumes x and epsilon int or float, power an int,
        epsilon>0&power>=1
    returns float y such that y**power is within epsilon of x.
        If such a float does not exist, it returns none"""
    if x < 0 and power%2==0:
        return None
    low = min(-1.0,x)
    high=max(1.0,x)
    ans=(high+low)/2.0
    while abs(ans**power-x)>=epsilon:
        if ans**power <x:
            low=ans
        else:
            high=ans
        ans=(high+low)/2.0
    return ans


def testFindRoot():
    epsilon = 0.0001
    for x in (0.25,-0.25,2,-2,8,-8):
        for power in range(1,4):
            print('Testing x=' + str(x) + ' and power = '+str(power))
            result = findRoot(x, power,epsilon)
            if result == None:
                print('no root')
            else:
                print('  ',  result**power, '~=', x)

