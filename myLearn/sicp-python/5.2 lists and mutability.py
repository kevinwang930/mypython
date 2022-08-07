# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 22:24:17 2018

@author: kevin
"""

Techs = ['MIT','Caltech']
Ivys = ['Harvard','Yale','Brown']
Univs = [Techs,Ivys]
Univs1 = [['MIT','Caltech'],['Harvard','Yale','Brown']]
print('Univs = ',Univs)
print('Univs1 = ',Univs1)
print('Id of Univs[0] and Univs[1]', id(Univs[0]), id(Univs[1])) 
print('Id of Univs1[0] and Univs1[1]', id(Univs1[0]), id(Univs1[1])) 
Techs.append('RPI')
print('Univs = ',Univs)  #mutuable lists

for e in Univs:
    print('Univs contains',e)
    print(' which contains')
    for u in e:
        print('   ',u)

L1 = [1,2,3]
L2 = [4,5,6]
L3= L1 + L2
print('l3 = ', L3)
L1.extend(L2)
print('L1 = ',L1)
L1.append(L2)
print('L1 = ',L1)