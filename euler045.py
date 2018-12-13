#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 23:36:36 2018

@author: edwin
"""
def isPentagonal(num):
    import math
    n = (math.ceil(math.sqrt(num*6)))//3
    return((n*(3*n-1))/2 == num)
    
def main():
    i = 144
    while 1:
        if(isPentagonal(i*(2*i-1))):
            return(i*(2*i-1))
        i= i+1