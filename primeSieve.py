#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 15:48:17 2018

@author: edwin
"""

def main(cap):
    primeList = []
    checkList = []
    for i in range (1,cap):
        checkList.append(1)
    for i in range(2,cap + 1):
        print(i)
        if checkList[i-2]:
            for j in range(2,cap//i + 1):
                checkList[(i*j)-2] = 0
    for k in range(0,cap-1):
        if (checkList[k] == 1):
            primeList.append(k+2)
    return primeList