# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 14:41:35 2018

@author: kevin
"""

import random

def collisionProb(n,k):
    prob = 1.0
    for i in range(1,k):
        prob = prob * ((n-i)/float(n))
    return 1 - prob

#print(collisionProb(1000,200))

def simInsertions(numIndices,numInsertions):
    """Assumes numIndices and numInsertions are positive ints
       Returns 1 if there is collision; 0 otherwise"""
    choices = range(numIndices)
    used = []
    for i in range(numInsertions):
        hashVal = random.choice(choices)
        if hashVal in used:
            return 1
        else:
            used.append(hashVal)
    return 0

def findProb(numIndices,numInsertions,numTrials):
    collisions = 0.0
    for t in range(numTrials):
        collisions += simInsertions(numIndices,numInsertions)
    return collisions/numTrials

print('Actual probability of a collision = ', collisionProb(1000,50))
print('Est. probability of a collision = ', findProb(1000,50,1000))
print('Actual probability of a collision = ', collisionProb(1000,200))
print('Est. probability of a collision = ', findProb(1000,200,1000))


