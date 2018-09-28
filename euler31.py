#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 20:23:53 2018

@author: edwin
"""

def changeWay(amount, coinList):
    coinList.sort
    if (len(coinList) == 0):
        return 0
    if (amount == 0):
        return 1
    if (amount < 0):
        return 0
    return changeWay((amount-coinList[-1]),coinList) + changeWay(amount,coinList[:-1])
            
def main(amount,coinList):
    print(changeWay(amount,coinList))