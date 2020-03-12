#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jean
#
# Created:     05/02/2018
# Copyright:   (c) Jean 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#import math
def isPrime(x):
	if x%2==0 and x>2: return False     # False for all even numbers
	i=3                                 # we don't divide by 1 or 2
	sqrt=x**.5
	while i<sqrt:
		if x%i==0: return False
		i+=2
	return True

# Part of find_inverse below
# See: http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
def eea(a,b):       #return Bézout's coefficients

    if b==0:return (1,0)
    (q,r) = (a//b,a%b)

    (s,t) = eea(b,r)
    print ("qr",q,r,end="; ")
    print("st",s,t,end="; ")
    print(t, s-(q*t) )
    return (t, s-(q*t))

# Find the multiplicative inverse of x (mod y)
# see: http://en.wikipedia.org/wiki/Modular_multiplicative_inverse
def find_inverse(x,y):
    print("appel de eea(%i,%i)" % (x,y))
    inv = eea(x,y)[0]

    extended_gcd(x,y)
    if inv < 1: inv += y #we only want positive values
    print("inv=",inv)
    print("test inverse=",(inv*x)%y)
    return inv

# See: http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm - Pseudocode
def extended_gcd(a, b):
    print("appel de extended_gcd(%i,%i)" % (a,b))
    #l'inverse de a modulo b est la valeur s quand r=1 (condition a,b premiers entre eux)
    s = 0;    old_s = 1
    t = 1;    old_t = 0
    r = b;    old_r = a
    print(old_r,"\t",old_s,"\t\t",old_t)
    print(r,"\t\t",s,"\t\t",t)
    while r != 0:
        quotient = old_r // r
        (old_r, r) = (r, old_r - quotient * r)
        (old_s, s) = (s, old_s - quotient * s)
        (old_t, t) = (t, old_t - quotient * t)
        print(r,"\t\t",s,"\t\t",t)
    print( "Bézout coefficients:", (old_s, old_t))
    print( "greatest common divisor:", old_r)
    print( "quotients by the gcd:", (s, t))
    if old_s<0:old_s+=b
    return (old_r,old_s,old_t)
def gcd(a,b):
    return extended_gcd(a,b)[0]
import sys
def main():
    P=97	# First prime
    Q=83	# Second prime
    E=179	# usually a constant; 0x10001 is common, prime is best
    #####################################################################
    # Make sure the numbers we picked above are valid.
    #####################################################################

    if not isPrime(P): raise Exception("P (%i) is not prime" % (P,))
    if not isPrime(Q): raise Exception("Q (%i) is not prime" % (Q,))

    T=(P-1)*(Q-1) # Euler's totient (intermediate result)
    # Assuming E is prime, we just have to check against T
    if E<1 or E > T: raise Exception("E must be > 1 and < T")
    print(extended_gcd(E,T))
    print("prime",T%E,E%T)
    if gcd(E,T)!=1: raise Exception("E is not coprime with T")

    #####################################################################
    # Now that we've validated our random numbers, we derive our keys.
    #####################################################################

    # Product of P and Q is our modulus; the part determines as the "key size".
    MOD=P*Q

    # Private exponent is inverse of public exponent with respect to (mod T)
    D = find_inverse(E,T)

    # The modulus is always needed, while either E or D is the exponent, depending on
    # which key we're using. D is much harder for an adversary to derive, so we call
    # that one the "private" key.
    print("P: %i, Q: %i, E: %i" % (P,Q,E))
    print ("public key: (MOD: %i, E: %i)" % (MOD,E))
    print ("private key: (MOD: %i, D: %i)" % (MOD,D))

    #print (eea(240,46),extended_gcd(240,46))
    #print(math.gcd(240,46))

    #extended_gcd(8,7)
    #extended_gcd(15,7)
    #extended_gcd(120,23)

    M=0

    while M==0:
        sys.stdout.write("? ")
        line=sys.stdin.readline().strip()
        if not line: break
        if line=='q' or line=='Q': break
        M=int(line)
        print(M)

    #print(pow(M,P-1,P))
    #print(pow(M,Q-1,Q))
    C=pow(M,E,MOD)
    print("C=",C)
    print("D=",D,extended_gcd(E,T)[1])
    R=pow(C,D,MOD)
    print(R)

if __name__ == '__main__':
    main()
