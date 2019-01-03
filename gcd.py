#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 02:27:22 2019

@author: edwin
"""

def main(x, y): 
  
   while(y): 
       x, y = y, x % y 
  
   return x 
