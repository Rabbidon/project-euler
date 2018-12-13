#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 15:02:45 2018

@author: edwin
"""

def main():
    import trialDivision
    import itertools
    for i in range (1000,10000):
        if trialDivision.main(i):
            numString = str(i)
            perms = list(set(list(''.join(p) for p in itertools.permutations(numString))))
            perms.sort()
            perms = perms[1 + perms.index(numString):]
            for j in perms:
                if(trialDivision.main(int(j)) and trialDivision.main(2*int(j) - i) and (str(2*int(j) - i) in perms)):
                    print(numString + j + str(2*int(j) - i))