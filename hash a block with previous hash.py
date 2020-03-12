#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
# Link : https://en.bitcoin.it/wiki/Block_hashing_algorithm
# Author:      Jean
#
# Created:     12/02/2018
# Copyright:   (c) Jean 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import hashlib                                                                   #les opérations se font qu'avec des bytes !!!!!
import codecs as cd

def rev3(a):
    return "".join(map(str.__add__, a[-2::-2] ,a[-1::-2]))

def rev6(a):
    return "".join([a[x:x+2] for x in range(0,len(a),2)][::-1])

def f(s): #recursive function
    return "" if not s else f(s[2:]) + s[:2]

#champs d'entête de blockchain bitcoin  en bytes
version=b"01000000"
hashPrevBlock=b"81cd02ab7e569e8bcd9317e2fe99f2de44d49ab2b8851ba4a308000000000000"
hashMerkleRoot= b"e320b6c2fffc8d750423db8b1eb942ae710e951ed797f7affc8892b0f1fc122b"
time= b"c7f5d74d"
bits= b"f2b9441a"
nonce= b"42a14695"
#entête de block d'un blockchain
header_hex = version + hashPrevBlock + hashMerkleRoot + time + bits +nonce       #type bytes OK
print("header_hex=",header_hex)
hash0=hashlib.sha256(header_hex).hexdigest()                                     #sha256 digère bytes et donne des bytes
print("sha256_header_hex=",hash0)                                                            #hexdigest donne une chaine str
# il faut préciser que le contenu est hex avec decode !
header_bin = cd.decode(header_hex, encoding='hex', errors='strict')              # encode une chaine hex et donne des bytes
print ("header_bin=",header_bin)
# sha256 1x
hash0=hashlib.sha256(header_bin).digest()
print("sha256_header_bin=",hash0)
# sha256 2x
hash1 = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
print("digest_sha2562x_header_bin=",hash1)
hash2 = hashlib.sha256(hashlib.sha256(header_bin).digest()).hexdigest()
print("hexdigest_sha2562x_header_bin=",hash2)
#'1dbd981fe6985776b644b173a4d0385ddc1aa2a829688d1e0000000000000000'
#reverse the hash  little indian ?
print("reverse_hexdigest_sha2562x_header_bin=",rev3(hash2))
#'00000000000000001e8d6829a8a21adc5d38d0a473b144b6765798e61f98bd1d'

#reverse hex string
#https://stackoverflow.com/questions/5864271/reverse-a-string-in-python-two-characters-at-a-time-network-byte-order
s='1dbd981fe6985776b644b173a4d0385ddc1aa2a829688d1e0000000000000000'
print(rev3(s))
print(rev6(s))
print(f(s))       #méthode récurssive !!!

def main():
    pass

if __name__ == '__main__':
    main()
