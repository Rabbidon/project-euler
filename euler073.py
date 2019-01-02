#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 21:09:17 2019

@author: edwin
"""
# We cannot use the same approch here as for the previous problem
# - which is prosumably why the required checking range is much less.

# Here we just factorise numbers in the range we want (store largest prime factor in each slot)

import math

def main(n):
    numGrid = [0 for i in range(n+1)]
    fracCounter = 0
    for i in range (2,len(numGrid)):
        # Using prime sieve, store largest prime factor of each number in range
        if numGrid[i] == 0:
            toEdit = i
            while toEdit<=n:
                numGrid[toEdit] = i
                toEdit += i
        factorSet = set()
        toEdit = i
        while toEdit>1:
            factorSet.add(numGrid[toEdit])
            toEdit//=numGrid[toEdit]
        # Test all numbers in range (n/3,n/2) for divisibility by each prime factor
        for j in range(1+(i//3),math.ceil(i/2)):
            addFlag = True
            for k in factorSet:
                if j%k == 0:
                    addFlag = False
                    break
            if addFlag:
                fracCounter += 1       
    return fracCounter
    
    
    