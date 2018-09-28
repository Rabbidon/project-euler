#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 17:20:29 2018

@author: edwin
"""

def main():
    import itertools
    digits = [1,2,3,4,5,6,7,8,9]
    perms = itertools.permutations(digits)
    for i in perms:
        if (i[0] * (1000*i[1]+100*i[2]+10*i[3]+i[4]) == 1000*i[5] + 100*i[6] + 10*i[7] + i[8]):
            print (1000*i[5] + 100*i[6] + 10*i[7] + i[8])
        if ((10*i[0]+i[1])*(100*i[2]+10*i[3]+i[4]) == 1000*i[5] + 100*i[6] + 10*i[7] + i[8]):
            print (1000*i[5] + 100*i[6] + 10*i[7] + i[8])