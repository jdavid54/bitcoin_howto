#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jean
#
# Created:     09/02/2018
# Copyright:   (c) Jean 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os

import hashlib

cwd=os.getcwd()
#print(cwd)
file_path = os.path.join(cwd, "hash file.py") #decimal incluant 2 entier 2.718
f = open(file_path, 'rb')
#print(tuple(f))
f.close()

f = open(file_path, 'rb')
text=f.read()
#print(type(text))     #type bytes avec open rb
#print(text)            #text rb : b'..............'
print('hash=',hashlib.sha256(text).hexdigest())      #le sha256 digère des bytes open(rb) et non pas des str open(r)
f.close()

def main():
    pass

if __name__ == '__main__':
    main()
