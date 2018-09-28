#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 16:56:33 2018

@author: edwin
"""

def findSolution(primeList,number,digits):
    if not primeList:
        print (int(digits[0] + number))
        return int(digits[0] + number)
    else:
        total = 0
        for i in digits:
            if ((int(i + number[:2])%(primeList[-1])) == 0):
                newDigits = digits.copy()
                newDigits.remove(i)
                total = total + findSolution(primeList[:-1],i + number,newDigits)
        return total

def main():
    total = 0
    primeList = [2,3,5,7,11,13]
    for i in range (100//17 + 1, 1000//17 + 1):
        digits = ['0','1','2','3','4','5','6','7','8','9']
        number = str(17*i)
        validFlag = 1
        for j in number:
            if j in digits:
                digits.remove(j)
            else:
                validFlag = 0
                break
        if validFlag:
            total = total + findSolution(primeList,number,digits)
    print(total)