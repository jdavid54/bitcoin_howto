#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        sha256 file
# Purpose:     calcule le sha256 des fichiers donnés en argument de ligne de commande : python sha256 filename1  filename2
# Link : https://gist.github.com/rji/b38c7238128edf53a181
# Author:      Jean
#
# Created:     13/02/2018
# Copyright:   (c) Jean 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import hashlib
import sys

def sha256_checksum(filename, block_size=65536):
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):                      #lire par bloc - permet de traiter des gros fichiers
            sha256.update(block)
    return sha256.hexdigest()

def main():                                                                      # le hash change
    for f in sys.argv[1:]:                                                       #installedpackages.txt
        print(f)                                                                  # 0351e85c7698f491bbb663415f3612e85c6f57e9ff89572901341b49e34c9d61
        checksum = sha256_checksum(f)                                            # installedpackages2.txt  modifié
        print(f + '\t' + checksum)                                                # cb3a60a1be4cfb432d81a29707f41b610798851c485490c7b30879f855580e86


if __name__ == '__main__':
    main()
