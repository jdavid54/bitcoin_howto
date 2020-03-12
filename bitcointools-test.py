#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jean
#
# Created:     13/02/2018
# Copyright:   (c) Jean 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from bitcointools import *

priv = random_key()
print(priv)
pub=privtopub(priv)
print(pub)
addr=pubtoaddr(pub)
print(addr)

priv = sha256('bitcoin is awesome lets all go to the moon someday')
print(priv)
pub=privtopub(priv)
print(pub)
addr=pubtoaddr(pub)
print(addr)

priv = sha256('bitcoin is awesome let all go to the moon someday')
print(priv)
pub=privtopub(priv)
print(pub)
addr=pubtoaddr(pub)
print(addr)

h=history('1NPrfWgJfkANmd1jt88A141PjhiarT8d9U')
print(h)

pub1= privtopub(random_key())
pub2= privtopub(random_key())
pub3= privtopub(random_key())
multi = mk_multisig_script(pub1,pub2,pub3,2,3)
print(multi)
maddr=scriptaddr(multi)
print(maddr)

def main():
    pass

if __name__ == '__main__':
    main()
