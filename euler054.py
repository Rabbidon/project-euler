#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 18:04:10 2018

@author: edwin
"""
def calculateScore(hand):
    from collections import Counter
    rankDict = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":11,"Q":12,"K":13,"A":14}
    ranks = sorted([rankDict[x[0]] for x in hand])
    suits = [x[1] for x in hand]
    rankDist = Counter(ranks)
    suitFlag = False
    if len(set(suits)) == 1:
        suitFlag = True
    if 4 in rankDist.values():
        score =  8
        scoreList = sorted(rankDist, key=lambda k: rankDist[k])
        scoreList.append(score)
        return(scoreList)
    elif 3 in rankDist.values() and 2 in rankDist.values():
        score =  7
        scoreList = sorted(rankDist, key=lambda k: rankDist[k])
        scoreList.append(score)
        return(scoreList)
    elif (ranks[4]==ranks[3]+1==ranks[2]+2==ranks[1]+3==ranks[0]+4):
        score = 5
        if suitFlag:
            score = 9
            if ranks[0] == 10:
                score = 10
        ranks.append(score)
        return(ranks)
    elif suitFlag:
        score = 6
        ranks.append(score)
        return(ranks)
    elif 3 in rankDist.values():
        score = 4
        scoreList = []
        for j in rankDist.keys():
            if rankDist[j] != 3:
                scoreList.append(j)
        sorted(scoreList)
        scoreList.append(ranks[2])
        scoreList.append(score)
        return(scoreList)
    elif len(set(ranks)) == 3:
        score = 3
        scoreList = []
        for j in rankDist.keys():
            if rankDist[j] != 2:
                scoreList.append(j)
        sorted(scoreList)
        scoreList.append(ranks[1])
        scoreList.append(ranks[3])
        scoreList.append(score)
        return(scoreList)
    elif 2 in rankDist.values():
        score = 2
        scoreList = []
        for j in rankDist.keys():
            if rankDist[j] != 2:
                scoreList.append(j)
            else:
                bookmark = j
        sorted(scoreList)
        scoreList.append(bookmark)
        scoreList.append(score)
        return(scoreList)
    else:
        score = 1
        ranks.append(score)
        return(ranks)

def determineWinner(inputList):
    hand1 = inputList[:5]
    hand2 = inputList[5:]
    score1 = calculateScore(hand1)
    score2 = calculateScore(hand2)
    compare = -1
    while True:
        if (score1[compare] > score2[compare]):
            return 1
        elif (score1[compare] < score2[compare]):
            return 0
        compare = compare - 1
    
def main(textfile):
    import time
    t = time.time()
    total = 0
    with open(textfile) as f:
        for line in f:
            total = total + determineWinner(line.split())
    print(time.time()-t)
    return total
            
    