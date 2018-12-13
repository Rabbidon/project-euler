#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 16:56:33 2018

@author: edwin
"""


#In theory this shouldn't be done with big integers in Python, since it defeats the point of the exercise,
#but this is a pretty dull question - just a more fiddly version of summing the digits of 2^1000, so I just bashed out a quick answer and moved on.

import math

def main():
	total = 0
	factorial = math.factorial(100)
	while factorial>0:
		total+=factorial%10
		factorial //=10
	print(total)