#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jean
#
# Created:     18/02/2018
# Copyright:   (c) Jean 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import hashlib
import binascii


# hash pairs of items recursively until a single value is obtained
def merkle(hashList):
    if len(hashList) == 1:
        return hashList[0]
    newHashList = []
    # process pairs; for odd length, the last is skipped
    for i in range(0, len(hashList)-1, 2):
        newHashList.append(hash2(hashList[i], hashList[i+1]))
    if len(hashList) % 2 == 1:   # odd, hash last item twice
        newHashList.append(hash2(hashList[-1], hashList[-1]))
    return merkle(newHashList)

def hash2(a, b):
    # reverse inputs before and after hashing
    # due to big-endian / little-endian nonsense
    a1 = binascii.unhexlify(a)[::-1]
    b1 = binascii.unhexlify(b)[::-1]
    h = hashlib.sha256(hashlib.sha256(a1 + b1).digest()).digest()
    return binascii.hexlify(h)[::-1]

#all the hashes codes in the block are hashed by pairs to get the merkle hash
txHashes = [
 '634192b589ea881333b5e566873ecbaaf8addc5d7ef4240f8e8c1325c29c4c7a'
,'26fe7c02081fa96999285aad651b4d7630586a0a95adf2481c9ccf7409422828'
,'f413cd85f36e50532f7ac66a54586197f246e2992cd5544291f7f096e7ced840'
,'d7969105839864d64bd2bfadfdd3d74239d6ca61c921ae7522d1efb572f656ea'
,'35c41399bf89c9c5930a2e828412056aea226e26d325ca6e1b18ffd54676273a'
,'c2fbb25c7dcca8a41e5b305e9ba0c0c9fcb80b16877029349b65358a7d7b7ce0'
,'8c406098409eb99638e768aa2ca920cc5ec056bdc3da19c6c39c4968e20ee000'
,'e162711f4f07794e70bd2004edf8fd61d349a9a9bd267c2b3f5973a7a84d95ef'
,'e41255088c4b217307c5460f36cd0ec891bdfdda12db96f6fb9832c0051d8751'
,'9ab30bb67fa2b3820fc18a7b78b6652d5222f70af64c0699f22894b25750bb99'
,'0000000000000000e067a478024addfecdc93628978aa52d91fabd4292982a50']
print(merkle(txHashes))

txHashes2 = [   #changing leading 6 into 0
 '034192b589ea881333b5e566873ecbaaf8addc5d7ef4240f8e8c1325c29c4c7a'
,'26fe7c02081fa96999285aad651b4d7630586a0a95adf2481c9ccf7409422828'
,'f413cd85f36e50532f7ac66a54586197f246e2992cd5544291f7f096e7ced840'
,'d7969105839864d64bd2bfadfdd3d74239d6ca61c921ae7522d1efb572f656ea'
,'35c41399bf89c9c5930a2e828412056aea226e26d325ca6e1b18ffd54676273a'
,'c2fbb25c7dcca8a41e5b305e9ba0c0c9fcb80b16877029349b65358a7d7b7ce0'
,'8c406098409eb99638e768aa2ca920cc5ec056bdc3da19c6c39c4968e20ee000'
,'e162711f4f07794e70bd2004edf8fd61d349a9a9bd267c2b3f5973a7a84d95ef'
,'e41255088c4b217307c5460f36cd0ec891bdfdda12db96f6fb9832c0051d8751'
,'9ab30bb67fa2b3820fc18a7b78b6652d5222f70af64c0699f22894b25750bb99'
,'0000000000000000e067a478024addfecdc93628978aa52d91fabd4292982a50']
print(merkle(txHashes2))

def main():
    pass

if __name__ == '__main__':
    main()
