#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 16:34:03 2018

@author: edwin
"""

def main(wordString):
    import math
    wordList = wordString.split("\",\"")
    wordTotal = 0
    for i in wordList:
        score = 0
        for j in i:
            score = score + (ord(j) - ord('A') + 1)
        n = math.floor(math.sqrt(score*2))
        if ((n*(n+1))/2 == score):
            wordTotal = wordTotal + 1
    print(wordTotal)