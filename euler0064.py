#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 17:04:43 2018

@author: edwin
"""

#This problem involves calcuating the continued fractions of square roots.
#This can be done naively, but here we will use a nice number theory result to remove the possibility of error
#when dealing with floating point arithmetic. We note that periodicity is guaranteed only when the remainders eventually repeat.

#We can show by induction that when calculating the expansion of sqrt(n), the remainder term will always be of the form

#   (sqrt(n)+a)/b

#where a,b are integers s.t. b divides n-a^2.

#For the base case, we have a = 0,b = 1, and 1 certainly divides n.

#For the inductive step, suppose we have (sqrt(n)+a)/b as a remainder term satisfying the above property.
#This is equal to (1/(b/(sqrt(n)+a))). The denominator is thus b/((sqrt(n)+a). The fractional part of this is the next remainder.

#Since, by assertion, b|(n-a^2), we have n-a^2 = k*b for some integer k. Let m be the floor of  b/((sqrt(n)+a).
#We now have, after some rearranging, remainder = (b*(sqrt(n)-a)-m*(n-a^2))/(n-a^2).
#This can be further rearranged to (sqrt(n) - (a+m*k))/k. We have n - (a+m*k)^2 = n-a^2 - k(2m+km^2).
#We see that this is a multiple of k since n-a^2 is. Therefore our new remainder is of the required form.

#This allows us modify the standard continued fraction recurrence relation, which is as follows:

#r_0 = sqrt(n)
#a_i = floor of r_i
#r_(i+1) = 1/(r_i - a_i) 

#The a_i are then terms in the continued fraction expansion. With our new knowledge, we can instead assert

#r_i = y_i/(sqrt(n)+x_i) = y_i*(sqrt(n)-x_i)/(n-(x_i)^2)

#(a_i has the same recurrence as before)

#with y_0 = n, x_0 = 0, and the recurrence relation y_(i+1) = (n-(x_i)^2)/(y_i), x_(i+1) = -(x_i + y_(i+1)*a_i).
#Now we can calculate i's until we encounter a pair x_i,y_i that we have encountered before.

import math

def main():
    oddTotal = 0
    for i in range(1,100):
        for j in range(1,i):
            xyPairs = []
            n = i*i+j
            x=0
            y=n
            a=i
            while [x,y] not in xyPairs:
                xyPairs.append([x,y])
                y = (n-x*x)//y
                x = -1*(x+a*y)
                a = y*(math.sqrt(n))//(n-x*x)
            if (len(xyPairs)-xyPairs.find([x,y]))%2 == 1:
                oddTotal += 1
    return oddTotal
                
            