#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jean
#
# Created:     18/02/2018
# Copyright:   (c) Jean 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import sys
import numpy as np

phi=1/2+np.sqrt(+5)


import hashlib
print(hashlib.sha3_256(b'hello world!').hexdigest())

print(hashlib.sha1(b'hello world!').hexdigest())

block ={
    'transactions':[
        {
            'from' : 'A',
            'to' : 'B',
            'amount' : 10
        },
        {
            'from' : 'B',
            'to' : 'C',
            'amount' : 10
        },
        {
            'from' : 'C',
            'to' : 'D',
            'amount' : 10,
            'message' : 'thanks for the help!'
        },
    ]
}

import pickle
pickle.dumps(block)
m = hashlib.sha3_256()
m.digest()
m.hexdigest()
block2 ={
    'transactions':[
        {
            'from' : 'A',
            'to' : 'B',
            'amount' : 1000000
        },
        {
            'from' : 'B',
            'to' : 'C',
            'amount' : 10
        },
        {
            'from' : 'C',
            'to' : 'D',
            'amount' : 10,
            'message' : 'thanks for the help!'
        },
    ]
}

n = hashlib.sha3_256()
n.update(pickle.dumps(block2))
n.hexdigest()
print(m.hexdigest())
print(n.hexdigest())

top_block ={
    'transactions':[
        {
            'from' : 'A',
            'to' : 'B',
            'amount' : 10
        },
        {
            'from' : 'B',
            'to' : 'C',
            'amount' : 10
        },
        {
            'from' : 'C',
            'to' : 'D',
            'amount' : 10,
            'message' : 'thanks for the help!'
        },
    ],
    'last_block' : m.hexdigest(),
    'nonce' : 0
}
print(top_block)
o = hashlib.sha3_256()
o.update(pickle.dumps(top_block))
o.hexdigest()
difficulty = 3
difficulty_string = ''.join(['0' for x in range(difficulty)])
print(difficulty_string)

#%%time

from pyspark.ml import Pipeline
from pyspark.ml.classification import LogisticRegression
import numpy as np
nonce = 1
top_block['nonce']=1
p = hashlib.sha3_256()
while p.hexdigest()[:difficulty] != difficulty_string:
    nonce += 1
    top_block['nonce'] = nonce
    p = hashlib.sha3_256()
    p.update(pickle.dumps(top_block))
print(nonce, p.hexdigest())
print(top_block)

def main():
    pass

if __name__ == '__main__':
    main()
