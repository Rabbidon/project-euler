#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 12:51:52 2018

@author: edwin
"""

def main():
    import trialDivision;
    maxChain = 0;
    storeI = 0;
    storeJ = 0;
    for i in range(-1000,1000):
        for j in range(-999,999):
            n = 0;
            while 1:
                evaluate = (n*n + j*n + i)
                if (evaluate <= 1):
                    if (n > maxChain):
                        maxChain = n
                        storeI = i
                        storeJ = j
                    break
                if (trialDivision.main(evaluate) == 0):
                    if (n > maxChain):
                        maxChain = n
                        storeI = i
                        storeJ = j
                    break
                n = n+1
    print (maxChain)
    print (storeI)
    print (storeJ)