#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 17:21:14 2019

@author: edwin
"""

# Here we just copy the previous problem, except that instead of all numbers we only permit primes. 

def main(threshold):
    primeList = []
    sumGrid = []
    sumGrid.append([])
    sumGrid.append([])
    counter = 2
    primeFlag = True
    while True:
        primeFlag = True
        sumGrid.append([])
        for i in primeList:
            subTotal = 0
            for k in range(min(len(primeList),len(sumGrid[-1-i]))):
                # The rule is we are only allowed to get new sums by adding new summands larger than any previous summand
                # This is achieved here by first deciding what number we will add (i) and then seeing how many sums with
                # summands all less than i sum to counter-i. We then add i to these to get all possible sums with largest term i
                # Doing this for all primes i<counter will give all prime sums totalling counter.
                if primeList[k]>i:
                    break
                subTotal += sumGrid[-1-i][k]
            sumGrid[-1].append(subTotal)
            if counter%i == 0:
                primeFlag = False
        if sum(sumGrid[-1])>threshold:
            return counter
        # Checking whether we have discovered a new prime
        if primeFlag:
            primeList.append(counter)
            sumGrid[-1].append(1)
        counter += 1