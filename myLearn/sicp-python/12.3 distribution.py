# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 11:54:10 2018

@author: kevin
"""

import pylab
import random

'''
vals = [1,200]
for i in range(1000):
    num1 = random.choice(range(1,100))
    num2 = random.choice(range(1,100))
    vals.append(num1+num2)
pylab.hist(vals,bins=10)
'''

def stdDev(X):
    """Assume X is a list of numbers.
       Returns the standard deviation of X"""
    mean = float(sum(X))/len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5    #Square root of mean difference

def CV(X):
    mean = sum(X)/float(len(X))
    try:
        return stdDev(X)/mean
    except ZeroDivisionError:
        return float('nan')
    
def flip(numFlips):
    heads = 0.0
    for i in range(numFlips):
        if random.random() < 0.5:
            heads +=1
    return heads/numFlips

def flipSim(numFlipsPerTrial, numTrials):
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads)/len(fracHeads)
    sd = stdDev(fracHeads)
    return (fracHeads,mean,sd)

def labelPlot(numFlips,numTrials,mean,sd):
    pylab.title(str(numTrials)+' Trials of '
                +str(numFlips)+ ' Flips each')
    pylab.xlabel('Fraction of Heads')
    pylab.ylabel('Number of Trials')
    xmin,xmax = pylab.xlim()
    ymin,ymax = pylab.ylim()
    pylab.text(xmin + (xmax-xmin)*0.02,(ymax - ymin)/2,
               'Mean = ' + str(round(mean,4))
               +'\nSD = '+str(round(sd,4)),size='x-large')

def makePlots(numFlips1,numFlips2,numTrials):
    val1,mean1,sd1 = flipSim(numFlips1,numTrials)
    pylab.hist(val1,bins = 100)
    xmin,xmax = pylab.xlim()
    ymin,ymax = pylab.ylim()
    labelPlot(numFlips1,numTrials,mean1,sd1)
    pylab.figure()
    val2,mean2,sd2 = flipSim(numFlips2,numTrials)
    pylab.hist(val2,bins = 100)
    pylab.xlim(xmin,xmax)
    labelPlot(numFlips2,numTrials,mean2,sd2)
    
def showErrorBars(minExp,maxExp,numTrials):
    """Assumes minExp and maxExp positive ints; minExp < maxExp
        numTrials a positive integer
        Plots mean fraction of heads with error bars"""
    means,sds = [],[]
    xVals = []
    for exp in range(minExp,maxExp + 1):
        xVals.append(2**exp)
        fracHeads,mean,sd = flipSim(2**exp,numTrials)
        means.append(mean)
        sds.append(sd)
    pylab.errorbar(xVals,means,yerr= 2*pylab.array(sds))
    pylab.semilogx()
    pylab.title('Mean Fraction of Heads(' + str(numTrials)+' trials)')
    pylab.xlabel('Number of flips per trial')
    pylab.ylabel('Fraction of heads & 95% confidence')
    
    
#random.seed(0)
#makePlots(100,1000,1000)
#showErrorBars(3,10,100)

def clear(n,p,steps):
    """Assumes n & steps positive ints, p a float
        n the initial number of molecules
        p the probability of a molecule being cleared
        exponential distribution"""
    numRemaining = [n]
    for t in range(steps):
        numRemaining.append(n*((1-p)**t))
    pylab.plot(numRemaining)
    pylab.semilogy()
    pylab.xlabel('Time')
    pylab.ylabel('Moleules Remaining')
    pylab.title('Clearance of Drug')
    
#clear(1000,0.01,1000)
    
def successfulStarts(eventProb,numTrials):
    """Assumes eventProb is a float representing a probability
        of a single attempt being successful. numTrials a positive int
        returns a list of the number of attempts needed before a 
        success for each trial."""
    triesBeforeSuccess=[]
    for t in range(numTrials):
        consecFailures = 0
        while random.random() > eventProb:
            consecFailures +=1
        triesBeforeSuccess.append(consecFailures)
    return triesBeforeSuccess

random.seed(0)
probOfSuccess = 0.5
numTrials = 5000
distribution = successfulStarts(probOfSuccess,numTrials)
pylab.hist(distribution,bins= 30)
pylab.xlabel('Tries Before Success')
pylab.ylabel('Number of Occurrences Out of '+str(numTrials))
pylab.title('Probability of Starting Each Try ' +str(probOfSuccess))



    