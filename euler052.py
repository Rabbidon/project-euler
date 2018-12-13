#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 16:52:14 2018

@author: edwin
"""

def euler52(digits):
    for i in range(10**(digits-1),(10**(digits))//6):
        for j in range(2,7):
            if sorted(str(i)) != sorted(str(i*j)):
                break
            print(j)
            if j == 6:
                return i
    if digits < 10:
        return euler52(digits+1)

def main():
    return euler52(6)
    