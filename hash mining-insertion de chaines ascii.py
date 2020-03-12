#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Jean
#
# Created:     14/02/2018
# Copyright:   (c) Jean 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import string
import random
import hashlib
import time

example_challenge = '9Kzs52jSfxjGJ54Sfjz5gZ111s'

def generation(challenge= example_challenge, size=25):
    answer = ''.join(random.choice(string.ascii_lowercase +
            string.ascii_uppercase + string.digits) for x in range(size))
    #print (challenge)
    #print (answer)

    attempt = challenge+answer
    #print( attempt)
    return attempt, answer

shaHash = hashlib.sha256()

def testAttempt(n):
    attempt, answer = generation()
    #print(attempt.encode('ascii'))
    shaHash.update(attempt.encode('ascii'))
    solution = shaHash.hexdigest()
    if solution.startswith('000'):
        print (n,attempt,'\n',solution)

def testAttempt2():
    Found = False
    n=1
    start = time.time()
    while Found == False:
        attempt, answer = generation()
        shaHash.update(attempt.encode('ascii'))
        solution = shaHash.hexdigest()
        if solution.startswith('0000'):
            timeTook = time.time() - start
            print (n,attempt,'\n',solution)
            print('time took: ', timeTook)
            Found = True
        n += 1

def main():
    #generation()
    """
    #method1
    for i in range(1000000):
        testAttempt2(i)
    """
    #method2
    testAttempt2()



if __name__ == '__main__':
    main()
