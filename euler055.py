#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 01:07:36 2018

@author: edwin
"""

def main():
    totalLychrel = 0
    for i in range(1,10001):
        summand = i
        lychrelFlag = True
        for k in range(1,51):
            summand = summand + int(str(summand)[::-1])
            if str(summand) == str(summand)[::-1]:
                lychrelFlag = False
                break
        if lychrelFlag:
            totalLychrel = totalLychrel + 1
    return totalLychrel
            