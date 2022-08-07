18.518.519.0# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 15:04:40 2018

@author: kevin
"""
import pylab
import numpy

def getData(fileName):
    dataFile = open(fileName,'r')
    distances = []
    masses = []
    discardHeader = dataFile.readline()
    for line in dataFile:
        d,m = line.split(' ')
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return (masses,distances)
def plotData(inputFile):
    masses,distances = getData(inputFile)
    masses = pylab.array(masses)
    forces = masses*9.81
    pylab.plot(forces,distances,'bo',label = 'Measured displacement')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('|force|(Newtons)')
    pylab.ylabel('Distance (Meters)')

#plotData('springData.txt')

def fitData(inputFile):
    masses,distances = getData(inputFile)
    distances = numpy.array(distances)
    masses = numpy.array(masses)
    forces = masses*9.81
    pylab.plot(forces,distances,'bo',label = 'Measured displacement')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('|Force| (Newtons)')
    pylab.ylabel('Distance (meters)')
    #find linear fit
    a,b = pylab.polyfit(forces,distances,1)
    predictedDistances = a*pylab.array(forces)+b
    k = 1.0/a
    pylab.plot(forces,predictedDistances,
               label = 'Displacements predicted by\nlinear fit, k = '
                       + str(round(k,5)))
    #find cubic fit
    a,b,c,d = pylab.polyfit(forces,distances,3)
    X = numpy.array([15])
    forces = numpy.append(forces,X)
    predictedDistances = a*(forces**3)+b*forces**2+c*forces+d
    
    pylab.plot(forces,predictedDistances,'b:',label = 'cubic fit')
    pylab.legend(loc = 'best')
    
fitData('springData.txt')