# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def main():
    import math
    import trialDivision
    i = 9
    while 1:
        successFlag = 1
        if not trialDivision.main(i):
            for j in range(1,math.ceil(math.sqrt(i//2))):
                if trialDivision.main(i - 2*(j**2)):
                    successFlag = 0
            if successFlag:
                print (i)
                break
        i = i+2