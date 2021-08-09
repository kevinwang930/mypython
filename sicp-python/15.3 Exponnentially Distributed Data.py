# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 13:50:20 2018

@author: kevin
"""
import math
import pylab
#define an arbitrary exponential function

def f(x):
    return 3*(2**(1.2*x))

def createExpData(f,xVals):
    """Assumes f is an exponential function of one argument
        xVals is an array of suitable arguments for f
        Returns array containing results of applying f to the 
        elements of xVals"""
    yVals = []
    for i in range(len(xVals)):
        yVals.append(f(xVals[i]))
    return pylab.array(xVals),pylab.array(yVals)

def fitExpData(xVals,yVals):
    """Try to find log(f(x),base) == ax +b"""
    logVals = []
    for y in yVals:
        logVals.append(math.log(y,2.0))
    a,b = pylab.polyfit(xVals,logVals,1)
    return a,b,2.0

xVals,yVals = createExpData(f,range(10))
pylab.plot(xVals,yVals,'ro',label = 'Actual values')
a,b,base = fitExpData(xVals,yVals)
predictedYVals = []
for x in xVals:
    predictedYVals.append(base**(a*x+b))
pylab.plot(xVals,predictedYVals,label = 'Predicted values')
pylab.title('Fitting an Exponential Function')
pylab.legend()
print('f(20) =',f(20))
print('Predicted f(20) =',base**(a*20 + b))
