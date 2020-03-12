#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Jean
#
# Created:     13/02/2018
# Copyright:   (c) Jean 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from bitcoin import *

priv = random_key()
print(priv)
pub=privtopub(priv)
print(pub)
addr=pubtoaddr(pub)
print(addr)

def main():
    pass

if __name__ == '__main__':
    main()
