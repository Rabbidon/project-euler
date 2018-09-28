#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 21:42:47 2018

@author: edwin
"""

def main():
    import trialDivision
    primes = 0
    counter = 1
    while (10*primes)>(4*counter-3) or counter<2:
        diagNumber = (2*counter-1)**2
        for i in range(4):
           diagNumber = diagNumber + 2*counter
           if trialDivision.main(diagNumber) == 1:
               primes = primes+1
        counter = counter+1
        print(primes/(4*counter-3))
    return (2*counter-1)