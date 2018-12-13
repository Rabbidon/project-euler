#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 23:31:46 2018

@author: edwin
"""

def concatenate(int1,int2):
    import trialDivision
    return trialDivision.main(int(str(int1)+str(int2))) == 1

def main():
    import trialDivision
    primeArray = []
    for i in range(1,10000):
        if (trialDivision.main(i) == 1):
            primeArray.append(i)
    primeAmount = len(primeArray)
    relationGrid = []
    for A in range(primeAmount):
        truthVector = []
        for B in range(primeAmount):
            if concatenate(primeArray[A],primeArray[B]):
                truthVector.append(1)
            else:
                truthVector.append(0)
        relationGrid.append(truthVector)
    for a in range(primeAmount):
        for b in range(a+1,primeAmount):
            if relationGrid[a][b] and relationGrid[b][a]:
                for c in range(b+1,primeAmount):
                    if relationGrid[a][c] and relationGrid[c][a] and relationGrid[b][c] and relationGrid[c][b]:
                          for d in range(c+1,primeAmount):
                              if relationGrid[a][d] and relationGrid[d][a] and relationGrid[b][d] and relationGrid[d][b] and relationGrid[c][d] and relationGrid[d][c]:
                                  for e in range(d+1,primeAmount):
                                      if relationGrid[a][e] and relationGrid[e][a] and relationGrid[b][e] and relationGrid[e][b] and relationGrid[c][e] and relationGrid[e][c] and relationGrid[d][e] and relationGrid[e][d]:
                                          print(primeArray[a])
                                          print(primeArray[b])
                                          print(primeArray[c])
                                          print(primeArray[d])
                                          print(primeArray[e])
                                  