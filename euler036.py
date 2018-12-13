#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:40:09 2018

@author: edwin
"""

def main(cap):
    total = 0
    for i in range (1,cap + 1):
        decString = str(i)
        binString = "{0:b}".format(i)
        if ((decString == decString[::-1]) and (binString == binString[::-1])):
            total = total + i
    print (total)