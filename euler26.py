# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def main(bound):
    maxLength = 0;
    for i in range(2,bound):
        digits = [];
        current = 10;
        carry = 0;
        carryList = []
        while 1:
            digits.append(current/i)
            carry = current%i
            if carry in carryList:
                if ((len(carryList) - carryList.index(carry)) > maxLength):
                    maxLength = len(carryList) - carryList.index(carry)
                    print (i)
                break
            carryList.append(carry)
            current = 10*carry
    print (maxLength)