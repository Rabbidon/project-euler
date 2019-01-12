#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 15:59:03 2019

@author: edwin
"""

# The only issue here is how to calculate the decimal expansions of square roots. I used the fact that
# sqrt is an increasing function and took a binary search-esque approach (I didn't use the actual
# binary search algorithm to avoid rounding errors - e.g if we have a number very close to 0.25,
# then it may take a very long time to determine whether the first digit should be 2 or 3 using the original
# binary search method

import math

def sqrt(n,d):
    # Gives the decimal expansion of n correct to d decimal places (rounded down).
    # Floats are unreliable so we use big ints to store the digits instead.
    if d == 0:
        return math.floor(math.sqrt(n))
    else:
        prev = sqrt(n,d-1)*10
        if (prev+5)**2 < n*(10**(2*d)):
            prev += 5
        if (prev+2)**2 < n*(10**(2*d)):
            prev += 2
        if (prev+1)**2 < n*(10**(2*d)):
            prev += 1
        if (prev+1)**2 < n*(10**(2*d)):
            prev += 1
    return prev

def decSum(expansion):
    # Sums the digits in our "expansion"
    total = 0
    while expansion > 0:
        total += expansion%10
        expansion //= 10
    return total
    
def main(n):
    total = 0
    for i in range(1,n):
        if math.floor(math.sqrt(i)) != math.sqrt(i):
            total += decSum(sqrt(i,99))
    return total
    
            
    