# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 15:35:10 2018

@author: kevin
"""
import random

class Item(object):
    def __init__(self,n,v,w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    
    def getName(self):
        return self.name
    
    def getValue(self):
        return self.value
    
    def getWeight(self):
        return self.weight
    
    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value)\
        + ', ' + str(self.weight) + '>'
        return result
    
def maxVal(toConsider, avail):
    '''Assumes toConsider a list of items, avail a weight
        Returns a tuple of total weight of a solution to the
        0/1 knapsack problem and the items of that solution'''
    print('maxVal begin',avail)
    for item in toConsider:
        print(item.getName())
    if toConsider == [] or avail == 0:
        result = (0,0,())
        withToTake = ()
    elif toConsider[0].getWeight() > avail:
        #explore left branch
        result = maxVal(toConsider[1:],avail)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal,withWeight,withToTake = maxVal(toConsider[1:],
                                    avail - nextItem.getWeight())
        withVal += nextItem.getValue()
        withWeight += nextItem.getWeight()
        withToTake = withToTake + (nextItem,)
        #Explore right branch
        withoutVal,withoutWeight,withoutToTake = maxVal(toConsider[1:],avail)
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal,withWeight,withToTake)
        else:
            result = (withoutVal,withoutWeight,withoutToTake)
    return result

def smallTest():
    names = ['a','b','c','d']
    vals = [6,7,8,9]
    weights = [3,3,2,5]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i],vals[i],weights[i]))
    val,taken = maxVal(Items,5)
    for item in taken:
        print(item)
    print('Total value of items taken =', val)
    
#smallTest()
    
def buildManyItems(numItems,maxVal,maxWeight):
    items = []
    for i in range(numItems):
        items.append(Item(str(i),
                          random.randint(1,maxVal),
                          random.randint(1,maxWeight)*random.random()))
    return items

def bigTest(numItems):
    items = buildManyItems(numItems,10,10)
    val,weight,taken = fastMaxVal(items,40)
    print('Items Taken')
    for item in taken:
        print(item)
    print('Total value of items taken =',val)
    print('Total weight of items taken =',weight)
    
def fastMaxVal(toConsider,avail,memo = {}):
    if (len(toConsider),avail) in memo:
        result = memo[(len(toConsider),avail)]
    elif toConsider == [] or avail == 0:
        result = (0,0,())
    elif toConsider[0].getWeight() > avail:
        result = fastMaxVal(toConsider[1:],avail,memo)
    else:
        nextItem = toConsider[0]
        withVal,withWeight,withToTake = fastMaxVal(toConsider[1:],
                                                   avail - nextItem.getWeight(),memo)
        withVal += nextItem.getValue()
        withWeight += nextItem.getWeight()
        withoutVal,withoutWeight,withoutToTake = fastMaxVal(toConsider[1:],
                                                            avail,memo)
        if withVal > withoutVal:
            result = (withVal,withWeight,withToTake + (nextItem,))
        else:
            result = (withoutVal,withoutWeight,withoutToTake)
    memo[(len(toConsider),avail)] = result
    return result

bigTest(1000)
        