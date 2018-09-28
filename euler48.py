#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 14:53:44 2018

@author: edwin
"""

def main(cap,digits):
    import truncMath
    total = 0
    for i in range (1,cap + 1):
        prod = 1
        for j in range (0,i):
            prod = truncMath.truncProduct(digits,prod,i)
        total = truncMath.truncSum(digits,total,prod)
    print(total)
    