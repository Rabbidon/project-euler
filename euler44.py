#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 22:17:54 2018

@author: edwin
"""
def isPentagonal(num):
    import math
    n = (math.ceil(math.sqrt(num*6)))//3
    return((n*(3*n-1))/2 == num)

def main():
    i = 2
    firstMatch = 0
    while not(firstMatch):
        iPent = (i*(3*i-1))//2
        for j in range(1,i):
            jPent = (j*(3*j-1))//2
            if (isPentagonal(iPent + jPent) and isPentagonal(iPent - jPent)):
                myJ = j;
                firstMatch = 1
                break
        i = i+1
    minDiff = iPent - jPent
    print(minDiff)
    cap = (minDiff//3) + 2
    for k in range(i,cap):
        for l in range(myJ,k):
            if (isPentagonal((k*(3*k-1))/2 - (l*(3*l-1))/2) and isPentagonal((k*(3*k-1))/2 + (l*(3*l-1))/2) and (k*(3*k-1))/2 - (l*(3*l-1))/2 < minDiff):
                minDiff = (k*(3*k-1))/2 - (l*(3*l-1))/2
    print(minDiff)