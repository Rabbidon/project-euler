#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 22:00:58 2018

@author: edwin
"""

#Since we are iterating up from 1, we can use the sieve of Eratosthenes to store what primes each number is divisible by.
#When we arrive at a prime p (array entry will be 0), we set the array entry of all multiples of p to p. If we arrive at a non-prime,
#then the array entry will be set to a prime dividing our number. We divide by this prime until we no longer can,
#and then use the multiplicativity of phi to quickly get  the totient function from this.

#This took a shade over a minute to run. I may try writing an implementation in C++ to see if I can do better.
 
def main(n):
    minPhi = n+1
    solution = 0
    numGrid = [0 for i in range (n+1)]
    for i in range (2,len(numGrid)):
        if numGrid[i] == 0:
            numGrid[i] = i-1
            toEdit = 2*i
            while toEdit<n+1:
                numGrid[toEdit] = i
                toEdit += i
            
        else:
            phi = 1
            toEdit = i
            while (toEdit%numGrid[i] == 0):
                toEdit //= numGrid[i]
                phi *= numGrid[i]-1
            if not (toEdit == 1):
                phi *= numGrid[toEdit]
            numGrid[i] = phi
            if "".join(sorted(str(phi))) == "".join(sorted(str(i))) and i/phi < minPhi:
                minPhi = i/phi
                solution = i
    return solution
        
                
    