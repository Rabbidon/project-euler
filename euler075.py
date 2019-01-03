#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 01:34:54 2019

@author: edwin
"""

# It is very impractical to find all Pythagorean triples in the required range by brute force, but there is another way.
# We generate all primitive Pythagorean triples as follows:

# Pick m>n s.t. m+n odd, gcd(m,n)=1. Then set a=m^2-n^2, b=2mn, c=m^2+n^2. It is clear that this gives
# a primitive Pythagorean triple, but not that it gives all of them. To see this, suppose that (a,b,c) is
# a primitive Pythagorean triple. Exactly one of a,b is even (squares can only be 0 or 1 mod 4 preventing both
# from being odd, and comprimality prevents both from being even). WLOG b is even. We note that

# c^2-a^2 = b^2 = (a+c)*(c-a)

# where a,c are necessarily both odd. We note also that (a+c),(c-a) share no odd factors: any factor shared by
# (a+c) and (c-a)  is also shared by 2a and 2c (addition and subtraction), which we know share no factors
# apart from the factor of 2 by assumption. This means that each prime power in b^2 goes entirely into 
# either (a+c) or (c-a), so in fact (a+c) and (c-a) are both twice a square. Therefore we write

# a+c = 2*m^2, c-a = 2*n^2

# and therefore a=m^2-n^2, b=2mn, c=m^2+n^2. All that remains to show is gcd(m,n) = 1 (trivial from a,c coprime)
# and m+n odd (m,n cannot have the same parity since this again violates a,c coprime). So we are done.

# All that remains now is to implement this knowlege in an algorithm:

import gcd
import math

def main():
    limit = 1500000
    sumCount = {}
    # We have a+b+c = 2m^2 + 2mn > 2m^2, so we need only test check m up to floor(sqrt(limit/2))
    for m in range(1,math.floor(math.sqrt(limit/2))):
        # m,n have different parity
        n = 1+(m%2)
        while n<m:
            #Establishing coprimality condition
            if gcd.main(m,n) == 1:
                #Taking care of nonprimitive triples
                sidelength = 2*m*m+2*m*n
                mult = 1
                while sidelength*mult <= limit:
                    sumCount[mult*(2*m*m+2*m*n)]= 1+sumCount.get(mult*(2*m*m+2*m*n),0)
                    mult += 1
            n += 2
    total = 0
    for i in sumCount:
        if sumCount.get(i) == 1:
            total += 1
    return total
    
    
    