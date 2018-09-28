#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 12:24:13 2018

@author: edwin
"""

def main(test):
    import math
    if (test == 1):
        return 0
    primeFlag = 1;
    for i in range (2,math.floor(math.sqrt(test))+1):
        if ((test%i) == 0):
             primeFlag = 0;
             break
    return primeFlag