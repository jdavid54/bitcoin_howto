#-------------------------------------------------------------------------------
# Name:        module1
# Purpose: Codage RSA
#
# Author:      Jean
#
# Created:     27/08/2017
# Copyright:   (c) Jean 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def cherche_b(a,z):
    b=0
    while (a*b)%z != 1 and b<z:
        b=b+1
    return b

def calcCode(M,a,n):
    C=1
    for k in range(a):
        C=C*M % n
    return C

def main():
    b=cherche_b(a,z)
    C=calcCode(30,a,n)
    D=calcCode(C,b,n)
    print(a,z,n,b,C,D)

if __name__ == '__main__':
    p=11; q=17
    n=p*q; z=(p-1)*(q-1)
    a=23;
    main()
