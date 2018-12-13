#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 19:49:05 2018

@author: edwin
"""

def main(power):
    mainTotal = 0
    for i in range(2,power*9**(power)):
        string = str(i)
        total = 0
        for j in range(0,len(string)):
            total = total + ((ord(string[j-1])-ord('0'))**power)
        if (total == i):
            mainTotal = mainTotal + total
    print (mainTotal)
        