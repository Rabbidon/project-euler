#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 15:44:54 2018

@author: edwin
"""

def main(gridSize):
    gridLine = gridSize*gridSize
    total = gridLine;
    counter = 2*(gridSize-1)+3
    while counter > 3:
        gridLine = gridLine - 2*(counter//4)
        total = total + gridLine
        counter = counter - 1
    print (total)
        
    