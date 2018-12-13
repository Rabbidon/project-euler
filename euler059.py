#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 21:58:49 2018

@author: edwin
"""

def decrypt(messageList,int1,int2,int3):
    decryptArray = [int1,int2,int3] 
    enumList = list(enumerate(messageList))
    decryptedList = [x[1]^decryptArray[(x[0]%3)] for x in enumList]
    decryptedMessage = ''.join([chr(x) for x in decryptedList])
    if(decryptedMessage.find(" the ")>-1) and (decryptedMessage.find(" and ")>-1):
        print(decryptedMessage)
        print(sum(decryptedList))

def main(encryptedMessage):
    with open(encryptedMessage) as f:
        for line in f:
            messageList = line.split(',')
            messageList = [int(x) for x in messageList]
            for int1 in range(ord('a'),ord('a')+27):
                for int2 in range(ord('a'),ord('a')+27):
                    for int3 in range(ord('a'),ord('a')+27):
                        decrypted = decrypt(messageList,int1,int2,int3)