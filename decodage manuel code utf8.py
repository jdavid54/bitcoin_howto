#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Jean
#
# Created:     12/02/2018
# Copyright:   (c) Jean 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def get_width(b):           #get_width avec des integers
    """
    calcule la longueur des séquences suivant le premier octet

    """
    if b <= 0x7f:
        return 1
    elif 0x80 <= b <= 0xbf:
        #Continuation byte
        raise ValueError('Bad alignment: %r is a continuation byte' % b)
    elif 0xc0 <= b <= 0xdf:
        return 2
    elif 0xe0 <= b <= 0xef:
        return 3
    elif 0xf0 <= b <= 0xf7:
        return 4
    else:
        raise ValueError('%r is not a single byte' % b)

def decode_utf8(utfbytes):
    start = 0
    uni = []
    while start < len(utfbytes):
        b = utfbytes[start]
        w = get_width(b)
        if w == 1:
            n = b
        else:
            n = b & (0x7f >> w)
            for b in utfbytes[start+1:start+w]:
                if not 0x80 <= b <= 0xbf:
                    raise ValueError('Not a continuation byte: %r' % b)
                n <<= 6
                n |= b & 0x3f
        uni.append(chr(n))
        start += w
    return ''.join(uni)


utfbytes = b'\xc2\xa9 \xc2\xae \xe2\x84\xa2'
print(utfbytes.decode('utf8'))
print(decode_utf8(utfbytes))

def main():
    pass

if __name__ == '__main__':
    main()
