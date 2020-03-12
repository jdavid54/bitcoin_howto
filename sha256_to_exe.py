#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jean
#
# Created:     03/03/2018
# Copyright:   (c) Jean 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import hashlib

message=input("PassPhrase :")
#"Hello world !"
msg=message.encode('ascii')

sha256 = hashlib.sha256()
sha256.update(msg)
code=sha256.hexdigest()
print(code)
message=input("Enter to close")
#hex: 2f951d3adf29ab254d734286755e2131c397b6fc1894e6ffe5b236ea5e099ecf
def main():
    pass

if __name__ == '__main__':
    main()
