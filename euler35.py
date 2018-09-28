#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 00:14:19 2018

@author: edwin
"""

def circularPrimes(length):
    import trialDivision
    digitSet = [1,3,7,9]
    total = 0
    for i in range (0,4**length):
        number = 0
        for k in range (0,length):
            number = number + (10**k)*digitSet[i%4]
            i = i//4
        primeFlag = 1
        for j in range (0,length):
            number = (10**(length-1))*(number%10) + number//10;
            if (trialDivision.main(number)==0):
                primeFlag = 0
                break
        if primeFlag:
            total = total+1
    return total
            
def main(length):
    total = 4
    for k in range (2, length+1):
        total = total + circularPrimes(k)
    print (total)