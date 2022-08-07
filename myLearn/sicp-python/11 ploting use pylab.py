# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 15:26:35 2018

@author: kevin
"""

import pylab
'''
pylab.figure(1)
pylab.plot([1,2,3,4],[1,7,3,5])
pylab.show()


pylab.figure(1)
pylab.plot([1,2,3,4],[1,2,3,4])
pylab.figure(2)
pylab.plot([1,4,2,3],[5,6,7,8])
pylab.savefig('kevin picture')
pylab.figure(1)
pylab.plot([5,6,10,3])
pylab.savefig('Figure-Jane')

'''

principal = 10000
interestRate = 0.05
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal*interestRate
pylab.rcParams['lines.linewidth'] = 4
pylab.rcParams['figure.figsize'] = (9,8)
pylab.rcParams['axes.titlesize'] = 16
pylab.rcParams['axes.labelsize'] = 13
pylab.rcParams['xtick.labelsize'] = 13
pylab.rcParams['ytick.labelsize'] = 13
pylab.rcParams['xtick.major.size'] = 7
pylab.rcParams['ytick.major.size'] = 7
pylab.rcParams['lines.markersize'] = 10

pylab.plot(values)
pylab.title('5% Growth, Compounded Annually')
pylab.xlabel('Years of Compounding')
pylab.ylabel('Value of Principal ($)')

