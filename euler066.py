#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 20:41:35 2018

@author: edwin
"""

#The third problem in a row on continued fractions - added by the same person at the same time, maybe?.
#It is a result in number theory that for any (x,y) solving x^-Dy^2=1, x/y is a convergent/
#It is another result that x_i-D(y_i)^2=1 or -1 occurs iff i is one less than a multiple of the repeating block length
#in the continued fraction expansion of sqrt(D), and that x_i/y_i alternates between over- and under-
#estimating D. The result is the following code:

import math

def main(n):
    maxP = 0
    solution = 0
    for i in range(1,n+1):
        if not (math.floor(math.sqrt(i))**2 == i):
            x = 0
            y = i
            marker = a = math.floor(math.sqrt(i))
            p_min = 1
            p_max = a
            q_min = 0
            q_max = 1
            parity = 1
            counter = 0
            #We reuse the code from Problem 64 to calculate quotients, except this
            #time we also calculate the convergents.
            while (a < 2*marker or parity<0):
                y = (i-x*x)//y
                x = (y*a-x)
                a = (y*(math.sqrt(i)+x))//(i-x*x)
                p_min,p_max = p_max,a*p_max + p_min
                q_min,q_max = q_max,a*q_max + q_min
                parity *= -1
                counter += 1
            if p_min>maxP:
                maxP = p_min
                solution = i
    return solution
            