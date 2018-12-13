#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 17:21:12 2018

@author: edwin
"""

def nChooseR(n,r):
    import math
    return math.factorial(n)//(math.factorial(r)*math.factorial(n-r))

def main():
    r = 10
    total = 0
    for n in range(23,101):
        while nChooseR(n,r)>=1000000:
            r = r-1
        total = total + n+1-2*(r+1)
    return (total)