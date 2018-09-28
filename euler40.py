#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 17:41:45 2018

@author: edwin
"""
def getDigit(position):
    i = 0
    j = 0
    while (i<position):
        i = i + 9*(j+1)*(10**(j))
        j = j + 1
    j = j - 1
    i = i - 9*(j+1)*(10**(j))
    digit = str(10**(j) + ((position - i - 1)//(j+1)))[((position - i - 1)%(j+1))]
    return (ord(digit)-ord('0'))

def main():
    return getDigit(1)*getDigit(10)*getDigit(100)*getDigit(1000)*getDigit(10000)*getDigit(100000)*getDigit(1000000)