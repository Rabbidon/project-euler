#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 14:28:16 2019

@author: edwin
"""

# This problem is theoretically identical to Problem 76. Unfortunately, the numbers involved in this case
# are far too large for our previous approach to work. Here I use a more efficient recurrence relation to 
# get the number of partitions using Euler's pentagonal theorem (which I will not go into here).

def main(mod):
    partitionNum = [1]
    count = 1
    while True:
        total = 0
        for i in range(1,count+1):
            if ((i*(3*i - 1))//2>count):
                break
            total += (2*(i%2)-1)*partitionNum[count-(i*(3*i - 1))//2]
            if ((i*(3*i + 1))//2>count):
                break
            total += (2*(i%2)-1)*partitionNum[count-(i*(3*i + 1))//2]
        total %= mod
        if total == 0:
            return count
        partitionNum.append(total)
        count += 1