#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 15:47:54 2018

@author: edwin
"""

def main(cap):
    import trialDivision
    primeList = []
    for i in range(1,cap):
        if trialDivision.main(i):
            primeList.append(i)
    sumList = []
    total = 0
    sumList.append(0)
    for j in primeList:
        total = total + j
        sumList.append(total)
    maxChain = 0
    maxPrime = 0
    for k in range(0,len(sumList)):
        for l in range(maxChain+1,k+1):
            if (sumList[k] - sumList[k-l])>cap:
                break
            if (trialDivision.main(sumList[k] - sumList[k-l])):
                maxChain = l
                maxPrime = sumList[k] - sumList[k-l]
    print(maxChain)
    print(maxPrime)