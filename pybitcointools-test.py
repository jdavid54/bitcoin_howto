#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      Jean
#
# Created:     13/02/2018
# Copyright:   (c) Jean 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from pybitcointools import *


def main():
    priv = random_key()
    print(priv)
    pub=privtopub(priv)
    print(pub)
    addr=pubtoaddr(pub)
    print(addr)

if __name__ == '__main__':
    main()
