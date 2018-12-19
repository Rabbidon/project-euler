# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import copy

def main():
    numSets = [[] for i in range(6)]
    #Store all relevant 4 digit cyclical figurate numbers,
    #keeping track of which type each number is.
    for j in range(3,9):
        i = 1
        n = 0
        while n+((j-2)*i - (j-3))<10000:
            n += ((j-2)*i - (j-3))
            i += 1
            if n>999:
                (numSets[j-3]).append(n)
    candidates = []
    #The idea from here is to investigate lists of numbers picked from these lists,
    #with at most one from each list, with the property that the last two digits of each element
    #are the first two digits of the next
    
    #We start with all valid lists of length 1 
        #(In fact, since we will be "joining" the two ends of the list
        #at the end, we can WLOG state that the first element is a triangular number)
    # and pick elements from lists we haven't accessed yet
    #in order to find all lists of length 6 with this property.
    for i in numSets[0]:
        candidates.append([{1,2,3,4,5},[i]])
    #We now check each of the remaining numbers (ones from lists we haven't pulled from yet)
    #and add them if the first two digits are the last two digits of the last number we picked.
    for iteration in range(5):
        newcandidates = []
        for i in candidates:
            for j in i[0]:
                for k in numSets[j]:
                    if (k//100) == ((i[1][-1])%100):
                        clone = copy.deepcopy(i)
                        clone[1].append(k)
                        clone[0].remove(j)
                        newcandidates.append(clone)
        candidates = newcandidates
    #The last thing to check is that the last two digits of the last entry are the first two digits of the first
    candidates = [i for i in candidates if (i[1][0])//100 == (i[1][-1])%100]
    print (candidates)
    print (sum(candidates[0][1]))
