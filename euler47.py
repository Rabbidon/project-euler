#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 14:28:20 2018

@author: edwin
"""

def main():
    i = 2
    counter = 0
    import factorise
    while counter < 4:
        if(len(factorise.main(i)) > 3):
            counter = counter + 1
        else:
            counter = 0
        i = i+1
    print(i - 4)
    