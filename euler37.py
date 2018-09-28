#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:52:21 2018

@author: edwin
"""

def main():
    import trialDivision
    total = 0
    ticks = 0
    i = 10
    while (ticks < 11):
        if (trialDivision.main(i)):
            forwardString = str(i)
            backwardString = forwardString
            successFlag = 1;
            for j in range(1,len(forwardString)):
                forwardString = forwardString[:-1]
                backwardString = backwardString[1:]
                if trialDivision.main(int(forwardString)) == 0 or trialDivision.main(int(backwardString)) == 0:
                    successFlag = 0
            if successFlag:
                print(i)
                total = total + i
                ticks = ticks + 1
        i = i + 1
    print(total)
                
        