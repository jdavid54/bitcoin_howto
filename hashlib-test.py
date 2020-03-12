#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jean
#
# Created:     11/02/2018
# Copyright:   (c) Jean 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
import hashlib
from hashlib import blake2b
print (sys.version)
print(sys.version_info)

m=hashlib.sha256()
m.update(b"Nobody inspects")
m.update(b" the spammish repetition!")
d=m.digest()
dh=m.hexdigest()
s=m.digest_size
bs=m.block_size
print(d,"\n",dh,"\n",s,"\n",bs)
print("Blake2")
#version 3.6
h = blake2b()
h.update(b'Hello world')
d=h.digest()
dh=h.hexdigest()
s=h.digest_size
bs=h.block_size
print(h,"\nd=",d,"\ndh=",dh,"\ns=",s,"\nbs=",bs)

def main():
    pass

if __name__ == '__main__':
    main()
