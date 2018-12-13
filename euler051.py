#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 15:16:40 2018

@author: edwin
"""

def main():
    import trialDivision
    import itertools
    import time
    t = time.time()
    i = 101
    while i<100000:
        print(i)
        numString = str(i)
        for j in itertools.combinations(range(5),2):
            baseList = ["*","*","*","*","*","*"]
            baseList[j[0]] = numString[0]
            baseList[j[1]] = numString[1]
            baseList[5] = numString[2]
            compositeCounter = 0
            for m in range(10):
                newList = [str(m) if x=="*" else x for x in baseList]
                result = int(''.join(newList))
                if (trialDivision.main(result) == 0) and (result>100000):
                    compositeCounter = compositeCounter + 1
                if compositeCounter > 2:
                    break
                if (compositeCounter < 2) and (m==9):
                    print(time.time()-t)
                    return result
        i=i+2