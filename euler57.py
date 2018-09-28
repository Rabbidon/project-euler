#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 21:37:34 2018

@author: edwin
"""

def main():
    num = 1
    denom = 1
    counter = 0
    for i in range(1,1001):
        num,denom = num+2*denom,num+denom
        if len(str(num))>len(str(denom)):
            counter = counter+1
    return counter