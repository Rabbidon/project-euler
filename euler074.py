#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 23:38:04 2019

@author: edwin
"""

# Basically here we just start at each nummber and apply the "factorial sum" function until we hit
# 169, 363601, 1454, 871, 45361, 872, 45362, or any number that is mapped to itself under this function.
# In fact we can do better - by flagging each number we have already dealt with and noting down the number
# of steps it takes to terminate, when we come to a number we have already encountered, we can work back
# to the beginning of the chain and fill in the step numbers as we go. This means we never do the same calculation twice.
# From here it is trivial to count the number of chains of length 60.

import math

def factorialSum(x):
    total = 0
    while x>0:
        total += math.factorial(x%10)
        x//=10
    return total
    
def main():
    count = 0
    #Initialise grid, and fill in numbers that we know terminate with their respective loop lengths.
    stepGrid = [0 for i in range(1000000)]
    stepGrid[169] = 3
    stepGrid[363601] = 3
    stepGrid[1454] = 3
    stepGrid[871] = 2
    stepGrid[45361] = 2
    stepGrid[872] = 2
    stepGrid[45362] = 2
    for i in range(1,1000000):
        #For each number, work out factorialSum until we reach a number we already dealt with.
        #We don't actually need to keep an explicit list - a counter would be fine - but a list is much better
        # for debugging purposes
        chain = []
        while True:
            if i<=1000000:
                if stepGrid[i]>0:
                    break
            chain.append(i);
            i = factorialSum(i)
            if i == chain[-1]:
                stepGrid[i] = 1
                break
        #We check if the chain has length 60
        if len(chain)+stepGrid[i] == 60:
            count += 1
        for j in range (len(chain)):
            if chain[j]<1000000:
                stepGrid[chain[j]]+=len(chain)-j+stepGrid[i]
    return count