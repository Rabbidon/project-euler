# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def main():
    import itertools
    import trialDivision
    digitList = [1,2,3,4,5,6,7]
    perms = itertools.permutations(digitList)
    maxNum = 0
    for i in perms:
        numString = ''.join(str(j) for j in i)
        num = int(numString)
        if (trialDivision.main(num)==1):
            maxNum = num
    print(maxNum)