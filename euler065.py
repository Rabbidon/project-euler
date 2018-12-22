#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 19:44:15 2018

@author: edwin
"""
#There is a standard approach which is to iteratively calculate convergents, but I was interested in finding a solution that didn't use this.
    
    #Since we have the luxury of knowing all quotients, we can work from the bottom of the fraction up:
    #We start with a_99 right at the bottom of the fraction. Call this f_99
    
    # We define a family of fractions f_i with numerator p_i and denominator q_i (in least form),
    # and relation f_(i-1) = a_(i-1)+1/f_(i) = (a_(i-1)*(p_i)+q_i)/p_i.
    # Note that if p_i and q_i are coprime, so too are p_i and a_(i-1)*p_i + q_i,
    # so in fact q_(i-1) = p_i and p_(i-1) = a_(i-1)*q_i + p_i. We have f_0 as our 100th convergent.
    
def main(n):
    denom = 1
    num = 1
    if (n-1)%3 == 2:
        denom = 2*n//3
    digitSum = 0
    for i in range (n-2):
        temp = denom
        denom = num
        a = 1
        if (n-2-i)%3 == 2:
            a = 2*(n-1-i)//3
        num = a*num + temp
    #The first quotient of e breaks the pattern of quotients, so we deal with it separately.
    temp = denom
    denom = num
    num = 2*num + temp
    while num>0:
        digitSum += num%10
        num //= 10
    return digitSum