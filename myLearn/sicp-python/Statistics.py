# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 17:12:57 2018

@author: kevin
"""
import pylab
import random


def rollDie():
    return random.choice([1,2,3,4,5,6])

def rollN(n):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    print(result)



def flip(numFlips):
    heads = 0.0
    for i in range(numFlips):
        if random.random() <0.5:
            heads +=1
    return heads/numFlips

def flipSim(numFlipsPerTrial, numTrials):
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads)/len(fracHeads)
    sd = stdDev(fracHeads)
    return (fracHeads,mean,sd)



def flipPlot(minExp,maxExp):
    ratios = []
    diffs = []
    xAxis = []
    for exp in range(minExp,maxExp+1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.random() < 0.5:
                numHeads += 1
        numTails = numFlips - numHeads
        ratios.append(numHeads/float(numTails))
        diffs.append(abs(numHeads-numTails))
    pylab.title('Difference Between Heads and Tails')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Abs(#heads - #tails)')
    pylab.semilogx()
    pylab.semilogy()
    pylab.plot(xAxis,diffs,'bo-')
    pylab.figure()
    pylab.title('Heads/Tails ratio')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('#heads/#tails')
    pylab.semilogx()
    pylab.semilogy()
    pylab.plot(xAxis,ratios,'bo-')




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


def makePlot(xVals,yVals,title,xLabel,yLabel,style,logX=False,logY=False):
    """Plots xVals vs. yVals with supplied titles and labels."""
    pylab.figure()
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.plot(xVals,yVals,style)
    if logX:
        pylab.semilogx()
    if logY:
        pylab.semilogy()

def runTrial(numFlips):
    numHeads = 0
    for n in range(numFlips):
        if random.random() < 0.5:
            numHeads += 1
    numTails = numFlips - numHeads
    return(numHeads,numTails)

def flipPlot1(minExp,maxExp,numTrials):
    """Assumes minExp and maxExp positive ints; minExp < maxExp
          numTrials a positive integer
       Plots summaries of results of numTrials trials of 
          2**minExp to 2**maxExp coin flips"""
    ratiosMeans,diffsMeans,ratiosSDs,diffsSDs,ratiosCVs,diffsCVs = [],[],[],[],[],[]
    xAxis = []
    for exp in range(minExp,maxExp+1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        ratios = []
        diffs = []
        for t in range(numTrials):
            numHeads,numTails = runTrial(numFlips)
            ratios.append(numHeads/float(numTails))
            diffs.append(abs(numHeads-numTails))
        ratiosMeans.append(sum(ratios)/float(numTrials))
        diffsMeans.append(sum(diffs)/float(numTrials))
        ratiosSDs.append(stdDev(ratios))
        diffsSDs.append(stdDev(diffs))
        ratiosCVs.append(CV(ratios))
        diffsCVs.append(CV(diffs))
    numTrialsString = ' ('+str(numTrials) + ' Trials'
    title = 'Mean heads/Tails Ratios' + numTrialsString
    makePlot(xAxis,ratiosMeans,title,
             'Number of Flips','Mean Heads/Tails','bo-',logX = True)
    title = 'Standard Deviation Heads/Tails Ratios' + numTrialsString
    makePlot(xAxis,ratiosSDs,title,
             'Number of Flips','Standard Deviation','bo-',
             logX = True, logY = True)
    title = 'Mean abs(#Heads-#Tails)' + numTrialsString
    makePlot(xAxis,diffsMeans,title,
             'Number of Flips','Mean abs(#Heads - #Tails)','bo-',
             logX = True, logY = True)
    title = 'SD abs(#Heads-#Tails)' + numTrialsString
    makePlot(xAxis,diffsSDs,title,
             'Number of Flips','Standard Deviation','bo-',
             logX = True, logY = True)
    title = 'Coeff. of Var. Heads/Tails Ratios' + numTrialsString
    makePlot(xAxis,ratiosCVs,title,
             'Number of Flips','Coeff. of Var','bo-',
             logX = True, logY = True)
    title = 'Coeff. of Var. abs(#Heads-#Tails)' + numTrialsString
    makePlot(xAxis,diffsCVs,title,
             'Number of Flips','Coeff. of Var.','bo-',
             logX = True, logY = True)

flipPlot1(4,20,20)
    

