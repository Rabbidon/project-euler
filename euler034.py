#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 18:23:20 2018

@author: edwin
"""

def main():
    import math
    mainTotal = 0
    for i in range(1,6*math.factorial(9)):
        numString = str(i)
        total = 0
        for j in numString:
            total = total + math.factorial(ord(j)-ord('0'))
        if (total == i):
            print (total)
            mainTotal = mainTotal + total
    print (mainTotal)
            