#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 17:04:43 2018

@author: edwin
"""

#We can use some number-theoretic results to make our lives easier here:

#Result 1: The first term in the repeated block of any integer square root is always the second term.
#Result 2: The last term in the repeated block of the expansion of sqrt(n)
#is the first instance of 2*(floor(sqrt(n))).
#Result 3: Each remainder we derive in the process is of the form (sqrt(n)-x)/y for integers x,y s.t.

# y|(n-x^2)

#This allows us to avoid rounding errors in our arithmetic by redefining the recurrence relation solely on integers..

#See this paper for proofs: http://web.math.princeton.edu/mathlab/jr02fall/Periodicity/mariusjp.pdf

import math

def main():
    oddTotal = 0
    #Iterating over all squares in range (1,10000)
    for i in range(1,100):
        for j in range(1,2*i+1):
            #Define n and initialise integer part and remainder terms
            n = i*i+j
            x = 0
            y = n
            a = marker = i
            counter = 0
            #Iteratively calculate the next integer parts and remainders until we hit the critical value.
            while not (a == 2*marker):
                y = (n-x*x)//y
                x = (y*a-x)
                a = (y*(math.sqrt(n)+x))//(n-x*x)
                counter += 1
            oddTotal += counter%2
    return oddTotal
                
            