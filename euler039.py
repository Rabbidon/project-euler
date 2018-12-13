#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:52:00 2018

@author: edwin
"""

def main(cap):
    import math
    numArray = []
    maxTotal = 0
    maxNumber = 0
    for testNum in range (1,cap+1):
        total = 0
        for a in range (1,testNum//2):
            c = ((a**2)+(testNum-a)**2)/(2*(testNum-a))
            if (math.floor(c)==c):
                total = total+1
        if (total > maxTotal):
            maxTotal = total
            maxNumber = testNum
    print(maxTotal//2)
    print(maxNumber)
    
        
            