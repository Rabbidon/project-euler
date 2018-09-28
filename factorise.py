#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 13:45:02 2018

@author: edwin
"""

def factorise(number,factorArray):
    import math
    if (number == 1):
        return factorArray
    if factorArray:
        if (number%(factorArray[-1][0]) == 0):
            factorArray[-1][1] = factorArray[-1][1] + 1
            return factorise(number//factorArray[-1][0],factorArray)
    lowerBound = 2
    if factorArray:
        lowerBound = factorArray[-1][0] + 1
    for i in range(lowerBound,1 + math.floor(math.sqrt(number))):
        if (number%i == 0):
            factorArray.append([i,1])
            return factorise(number//i, factorArray)
    factorArray.append([number,1])
    return factorArray

def main(number):
    return factorise(number,[])