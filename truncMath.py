#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 14:37:48 2018

@author: edwin
"""

def truncSum(digits,int1,int2):
    return (int1 + int2)%(10**digits)

def truncProduct(digits,int1,int2):
    return (int1*int2)%(10**digits)