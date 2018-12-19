#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 18:21:12 2018

@author: edwin
"""

def main():
    i = 100
    digits = 7
    frequencies = {}
    minRep = {}
    while True:
        #Calculating cubes in ascending order
        iCubed = i*i*i
        #When we reach a new digit threshold, none of the cubes in our previous set
        # will have any larger cubic permutations, so we can check to see whether any of them
        #has exactly 5 cubic permutations. If so, then we accept the earliest such entry in our dictionary.
        if iCubed >= 10**digits:
            for j in frequencies:
                if frequencies[j] == 5:
                    return minRep[j]
            digits += 1
            frequencies = {}
            minRep = {}
        #We order the digits of the cubes and enter them into a dictionary, incrementing the counter instead
        #if the string of ordered digits has been seen before
        sortedCube = ''.join(sorted(str(iCubed)))
        frequencies[sortedCube] = frequencies.get(sortedCube,0)+1
        #We store the least cube corresponding to each string of ordered digits so that we can return it if needed.
        minRep[sortedCube] = minRep.get(sortedCube,iCubed)
        i += 1
        