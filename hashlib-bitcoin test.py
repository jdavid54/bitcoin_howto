#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
# Link : https://www.youtube.com/watch?v=2Nih24Hy5ng
# Author:      Jean
#
# Created:     13/02/2018
# Copyright:   (c) Jean 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import hashlib
m = hashlib.sha3_256()
m.update(b'hello world!')
#print(m.digest())
#print(m.hexdigest())

n = hashlib.sha3_256()
n.update(b'hello world! hello world! hello world! hello world! hello world! hello world! hello world!')
#print(n.digest())
#print(n.hexdigest())

print(m.hexdigest())
print(n.hexdigest())

def main():
    pass

if __name__ == '__main__':
    main()
