#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:     Cryptage ADFGVX
#
# Author:      Jean
#
# Created:     04/03/2018
# Copyright:   (c) Jean 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np
#N=6
#t=np.random.random((N,N))
#print(t)
S="ADFGVX"
s="abcdefghijklmnopqrstuvwxyz0123456789"
new = False

def niceprint(dict):
    print(' ','A','D','F','G','V','X')
    for i in S:
        print(str(i),end=' ')
        for j in S:
            print(dict[str(i)+str(j)],end=' ')
        print()
    print()

def savedict(dict):
    np.save('mydict.npy',dict)
    print('Dictionary saved')

def loaddict():
    return np.load('mydict.npy').item()

def createrandomdict():
    import random

    #print(len(s))
    alphabet=''.join(random.sample(s,len(s)))
    #print(alphabet)


    dict={}
    k=0
    for i in S:
        for j in S :
            dict[str(i)+str(j)]=alphabet[k]
            k+=1
    print("Save dictionary in file")
    savedict(dict)
    return dict

def encoding(msg, dict, mode='ENCODE'):
    encodemsg=''
    if mode=='ENCODE':
        print('ENCODING :',msg)
        for p in range(0,len(msg)):
            if msg[p] in s:
                encodemsg+=((dict[msg[p]]))
        return encodemsg
    else :
        print('DECODING :',msg)
        for p in range(0,len(msg),2):
                encodemsg+=((dict[msg[p:p+2]]))
        return encodemsg

def transpo(s):
    encodemsg=''
    keydict={}
    key=list('maison')              #key en clair
    keysorted=sorted(key)
    #print(key, keysorted)           #key.sort() donne None !!!
    #il faut écrire le message à envoyer dans l'ordre de la clé key puis envoyer dans l'ordre keysorted en clair
    start=0
    print("Message avant transpo :",s)
    for k in key:
        #print(k,': ',end='')
        keydict[k]=''
        for p in range(start,len(s),12):
            #print (s[p:p+2],end='')
            keydict[k]=keydict[k]+s[p:p+2]
        start+=2
        #print()
    #print(keydict)
    for p in range(0,len(s)//6,2):
        #print(p)
        for k in keysorted:
            #print(k,': ',end='')
            encodemsg+=((keydict[k][p:p+2]))
    print("Message après transpo :",encodemsg)
    control=inv_transpo(encodemsg)
    #print(control)
    return encodemsg

def inv_transpo(s):
    encodemsg=''
    keydict={}
    key=list('maison')              #key en clair
    keysorted=sorted(key)
    #print(key, keysorted)           #key.sort() donne None !!!
    #il faut écrire le message reçu dans la clé keysorted puis permuter les colonnes dans l'ordre key en clair
    start=0
    print("Message avant transpo inverse :",s)
    for k in keysorted:
        #print(k,': ',end='')
        keydict[k]=''
        for p in range(start,len(s),12):
            #print (s[p:p+2],end='')
            keydict[k]=keydict[k]+s[p:p+2]
        start+=2
        #print()
    #print(keydict)
    for p in range(0,len(s)//6,2):
        #print(p)
        for k in key:
            #print(k,': ',end='')
            encodemsg+=((keydict[k][p:p+2]))
    print("Message après transpo inverse :",encodemsg)
    return encodemsg

def main():
    if new :
        mydict=createrandomdict()
    else:
        print('Load dictionary')
        mydict=loaddict()

    #print(mydict)
    niceprint(mydict)
    inv_dict = {v: k for k, v in mydict.items()}
    #print(inv_dict)

    msg=encoding("hello world!hello world!hello world!",inv_dict)
    print(msg)
    decodemsg=encoding(msg,mydict,mode='DECODE')
    print(decodemsg,'\n')
    #tranposition
    encodemsg=transpo(msg)
    print("Message envoyé :",encodemsg)

if __name__ == '__main__':
    main()
