#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 14:54:22 2018

@author: edwin
"""

import math

def main():
    power = 1
    total = 0
    #We look for integers n,k s.t 10^(k-1)<=n^k<10(k).
    #We can simplify this condition to 10^((k-1)/k)<n<10 by taking kth roots.
    #We then work out all integers n in this range for increasingly large k,
    #stopping when 9<=10((k-1)/k).
    while (9**power)>(10**(power-1)):
        total += math.floor(10-(10**((power-1)/power)))
        power += 1
    return total