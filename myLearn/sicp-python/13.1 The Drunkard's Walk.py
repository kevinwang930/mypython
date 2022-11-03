# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 11:56:32 2018

@author: kevin
"""

import random
import pylab


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

class Location(object):
    def __init__(self,x,y):
        """x and y are floats"""
        self.x = x
        self.y = y
    
    def move(self,deltaX,deltaY):
        return Location(self.x + deltaX,self.y +deltaY)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distFrom(self,other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5
    
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'
    
class Field(object):
    
    def __init__(self):
        self.drunks = {}
        
    def addDrunk(self,drunk,loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
    
    def moveDrunk(self,drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        xDist,yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        #use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist,yDist)
    
    def getLoc(self,drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]
    
class Drunk(object):
    def __init__(self,name = None):
        self.name = name
        
    def __str__(self):
        if self !=None:
            return self.name
        return 'Anonymous'
    
class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices=[(0.0,1.0),(0.0,-1.0),(1.0,0.0),(-1.0,0.0)]
        return random.choice(stepChoices)
    
def walk(f,d,numSteps):
    """Assumes: f a Field,d a Drunk in f,and numsteps an int >= 0.
       Moves d numSteps times, and return the difference between
       the final location and the location at the start of the walk"""
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))
    
def simWalks(numSteps,numTrials,dClass):
    """Assumes numSteps an int >= 0,numTrials an int >= 0
        dClass a subclass of Drunk
        Simulates numTrials walks of numSteps steps each
        Returns a list of the final distances for each trial"""
        
    Homer = dClass()
    origin = Location(0.0,0.0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer,origin)
        distances.append(walk(f,Homer,numSteps))
    return distances

def drunkTest(walkLengths,numTrials,dClass):
    """Assumes walkLengths a sequence of ints >=0
        numTrials an int > 0, dClass a subclass of Drunk
        For each number of steps in WalkLengths, runs simWalks with
         numTrials walks and prints results"""
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials,dClass)
        print(dClass.__name__, 'random walks of ',numSteps,' steps')
        print(' Mean =',sum(distances)/len(distances),\
              'CV =',CV(distances))
        print(' max =', max(distances),'Min =',min(distances))
        
#drunkTest((0,10,100,1000,10000),100,UsualDrunk) 

class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0,1.0),(0.0,-2.0),(1.0,0.0),(-1.0,0.0)]
        return random.choice(stepChoices)
    
class EWDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(1.0,0.0),(-1.0,0.0)]
        return random.choice(stepChoices)


        
#simAll((UsualDrunk,ColdDrunk,EWDrunk),(100,1000),10)

class styleIterator(object):
    def __init__(self,styles):
        self.index = 0
        self.styles = styles
        
    def nextStyle(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) -1:
            self.index = 0
        else:
            self.index +=1
        return result
    
def simDrunk(numTrials,dClass, walkLengths):
    meanDistances = []
    cvDistances = []
    for numSteps in walkLengths:
        print('Starting simulation of ',numSteps,' steps')
        trials = simWalks(numSteps,numTrials,dClass)
        mean = sum(trials)/len(trials)
        meanDistances.append(mean)
        cvDistances.append(stdDev(trials)/mean)
    return (meanDistances,cvDistances)

def simAll(drunkKinds,walkLengths,numTrials):
    styleChoice = styleIterator(('b-','r:','m-.'))
    for dClass in drunkKinds:
        curStyle = styleChoice.nextStyle()
        print('Starting simulation of ',dClass.__name__)
        means,cvs = simDrunk(numTrials,dClass,walkLengths)
        cvMean = sum(cvs)/len(cvs)
        pylab.plot(walkLengths,means,curStyle,
                   label = dClass.__name__ +
                   '(CV= ' + str(round(cvMean,4)) + ')')
    pylab.title('Mean distance from Origin ('
                + str(numTrials) + ' Trials)')
    pylab.xlabel('Number of Steps')
    pylab.ylabel('Distance from Origin')
    pylab.legend(loc = 'best')
    pylab.semilogx()
    pylab.semilogy()
    
#simAll((UsualDrunk,ColdDrunk,EWDrunk),(10,100,1000,10000,100000),100)

def getFinalLocs(numSteps,numTrials,dClass):
    locs = []
    d = dClass()
    origin = Location(0,0)
    for t in range(numTrials):
        f = Field()
        f.addDrunk(d,origin)
        for s in range(numSteps):
            f.moveDrunk(d)
        locs.append(f.getLoc(d))
    return locs

def plotLocs(drunkKinds,numSteps,numTrials):
    styleChoice = styleIterator(('b+','r^','mo'))
    for dClass in drunkKinds:
        locs = getFinalLocs(numSteps,numTrials,dClass)
        xVals,yVals = [],[]
        for l in locs:
            xVals.append(l.getX())
            yVals.append(l.getY())
        meanX = sum(xVals)/float(len(xVals))
        meanY = sum(yVals)/(float(len(yVals)))
        curStyle = styleChoice.nextStyle()
        pylab.plot(xVals,yVals,curStyle,
                      label = dClass.__name__ + ' Mean loc.= <'
                      + str(meanX)+', '+str(meanY) + '>')
    pylab.title('Location at End of Walks ('
                + str(numSteps) + ' steps)')
    pylab.xlabel('steps East/West of Origin')
    pylab.ylabel('steps North/South of Origin')
    pylab.legend(loc = 'Lower left',numpoints = 1)
    
#plotLocs((UsualDrunk,ColdDrunk,EWDrunk),100,200)
class oddField(Field):
    def __init__(self,numHoles,xRange,yRange):
        Field.__init__(self)
        self.wormholes = {}
        for w in range(numHoles):
            x = random.randint(-xRange,xRange)
            y = random.randint(-yRange,yRange)
            newX = random.randint(-xRange,xRange)
            newY = random.randint(-yRange,yRange)
            newLoc = Location(newX,newY)
            self.wormholes[(x,y)] = newLoc
            
    def moveDrunk(self,drunk):
        Field.moveDrunk(self,drunk)
        x = self.drunks[drunk].getX()
        y = self.drunks[drunk].getY()
        if (x,y) in self.wormholes:
            self.drunks[drunk] = self.wormholes[(x,y)]
            
def traceWalk(drunkKinds,numSteps):
    styleChoice = styleIterator(('b+','r^','mo'))
    f = oddField(1000,100,200)
    for dClass in drunkKinds:
        d = dClass()
        f.addDrunk(d,Location(0,0))
        locs = []
        for s in range(numSteps):
            f.moveDrunk(d)
            locs.append(f.getLoc(d))
        xVals = []
        yVals = []
        for l in locs:
            xVals.append(l.getX())
            yVals.append(l.getY())
        curStyle = styleChoice.nextStyle()
        pylab.plot(xVals,yVals,curStyle,label = dClass.__name__)
        pylab.title('Spots Visited on Walk ('
                       + str(numSteps) + ' Steps)')
        pylab.xlabel('Steps East/West of Origin')
        pylab.ylabel('Steps North/South of Origin')
        pylab.legend(loc = 'best')
        
#traceWalk((UsualDrunk,ColdDrunk,EWDrunk),200)
        

            
traceWalk((UsualDrunk,ColdDrunk,EWDrunk),500)









    