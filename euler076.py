#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 15:02:29 2019

@author: edwin
"""
# To differentiate between reorderings of the same sum, we can make sure that we deal with all sums with
# terms in some consistent order (such as increasing or decreasing). This implementation keeps ordering by
# dealing with summands in decreasing order - minAmount tracks the greatest summand used 
# thus far and only allows new summands at least this large.

# The rest of the code is for caching - running the above naively involves repeating the same calculations
# over and over - so instead we create an array of 100 elements. The nth slot consists of an array of length n,
# with the ith slot in this array representing the number of sums totalling n with greatest summand i.


import math

def main(n):
    sumGrid = []
    sumGrid.append([])
    for i in range(1,n+1):
        #Initialise the empty arrays
        sumGrid.append([0 for j in range(i)])
        for j in range (1,i):
            for k in range(min(j,i-j)):
                # The rule is we are only allowed to get new sums by adding new summands larger than any previous summand
                # This is achieved here by first deciding what number we will add (i-j) and then seeing how many sums with
                # summands all less than i-j sum to j. We then add i-j to these to get all possible sums with largest term i-j.
                # Doing this for all j<i will give all sums totalling i.
                sumGrid[i][i-j-1] += sumGrid[j][k]
        sumGrid[i][i-1] = 1
    return sum(sumGrid[n])-1