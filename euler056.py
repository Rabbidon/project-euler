#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 19:38:37 2018

@author: edwin
"""

def main():
    maxDigitSum = 0
    for i in range(1,101):
        product = 1
        for j in range(1,101):
            product = product*i
            digits = [int(x) for x in str(product)]
            digitSum = sum(digits)
            if digitSum > maxDigitSum:
                maxDigitSum = digitSum
    return maxDigitSum