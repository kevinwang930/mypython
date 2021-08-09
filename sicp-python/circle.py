# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 23:44:47 2018

@author: kevin
"""

pi = 3.14159
def area(radius):
    return pi*(radius*2)

def circumference(radius):
    return 2*pi*radius

def sphereSurface(radius):
    return 4.0*area(radius)