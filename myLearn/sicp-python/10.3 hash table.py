# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 17:31:06 2018

@author: kevin
"""

class intDict(object):
    """A dictionery with integer keys"""
    def __init__(self,numBuckets):
        """Create an empty dictionery"""
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])
            
    def addEntry(self,dictKey,dictVal):
        """Assumes dictKey an int. Adds an entry"""
        hashNo = dictKey%self.numBuckets
        hashBucket = self.buckets[hashNo]
        for i in range(len(hashBucket)):
            k = hashBucket[i][0]
            if k == dictKey:
                hashBucket[i] = (dictKey, dictVal)
                return
        hashBucket.append((dictKey,dictVal))
    
    def getValue(self,dictKey):
        """Assumes dictKey an int. Returns entry associated
           with the key dictKey"""
        hashNo = dictKey%self.numBuckets
        hashBucket = self.buckets[hashNo]
        for e in hashBucket:
            if e[0] == dictKey:
                return e[1]
        return None
    def __str__(self):
        result = '{'
        for b in self.buckets:
            for e in b:
                result = result + str(e[0]) +':' + str(e[1]) + ','
        return result[:-1] + '}'
            
import random

D=intDict(29)
for i in range(20):
    key = random.randint(0,10**5)
    D.addEntry(key,i)
print(D)
print('\n','The buckets are:')
for hashBucket in D.buckets:
    print('  ',hashBucket)