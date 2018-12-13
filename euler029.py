#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 17:19:10 2018

@author: edwin
"""

def main(bound):
    import math
    checklist = []
    total = 0;
    for i in range(0,bound+1):
        checklist.append(1)
    for j in range(2,bound+1):
        if checklist[j-1]:
            cap = math.floor(math.log(bound,j))
            if (cap>1):
                for k in range(2,cap + 1):
                    checklist[(j**k)-1] = 0
                for l in range(2,cap*bound + 1):
                    for m in range((l+bound-1)//bound,cap + 1):
                        if (l%m == 0):
                            total = total + 1
                            break
            else:
                total = total + (bound -1)
    print (total)
            
                        
        
    