#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Jean
#
# Created:     27/08/2017
# Copyright:   (c) Jean 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def cherche_lettres():
    global lettres,val_lettres,num
    for k in range(len(a)):
        for j in range(len(a[k])):
            if a[k][j] not in lettres:
                lettres=lettres+a[k][j]
                val_lettres.append(0)
    for k in range(len(a)):
        nummot=[]
        for j in range(len(a[k])):
            n=lettres.find(a[k][j])
            nummot.append(n)
        print(a[k],nummot)
        num.append(nummot)
    print (lettres,val_lettres,num)

def tous_differents():
    #global val_lettres
    k=0
    #print(val_lettres)
    n=len(val_lettres)
    ok=True
    while k<n-1 and ok:
        j=k+1
        u=val_lettres[k]
        while  j<n and ok:
            ok=(ok and u != val_lettres[j])
            j=j+1
        k=k+1
    return ok

def calcul_operation():
    global found,result
    r=[0,0,0]
    for k in range(len(a)):
        N=''
        for j in range(len(num[k])):
            N=N+str(val_lettres[num[k][j]])
        r[k]=int(N)
        #print(a,r)
    if r[0]+r[1]==r[2]:
        found+=1
        result.append(val_lettres)
        result.append(r)
        #print(result)
        print (r)
        print (found,"->",lettres,"=",val_lettres)



def main():
    global val_lettres
    cherche_lettres()
    a0,a1,a2,a3,a4,a5,a6,a7=[0,0,0,0,0,0,0,0]
    first=True
    for a0 in range(0,10):
        index=[a0,0,0,0,0,0,0,0]
        if not first:
            del(index[index.index(a0)])
            if a0 in index:continue
        #print (a0)
        for a1 in range(10):
            first=False
            index=[a0,a1,a2,a3,a4,a5,a6,a7]
            del(index[index.index(a1)])
            if a1 in index:continue
            for a2 in range(10):
                index=[a0,a1,a2,a3,a4,a5,a6,a7]
                del(index[index.index(a2)])
                if a2 in index:continue
                for a3 in range(10):
                    index=[a0,a1,a2,a3,a4,a5,a6,a7]
                    del(index[index.index(a3)])
                    if a3 in index:continue
                    for a4 in range(10):
                        index=[a0,a1,a2,a3,a4,a5,a6,a7]
                        del(index[index.index(a4)])
                        if a4 in index:continue
                        for a5 in range(10):
                            index=[a0,a1,a2,a3,a4,a5,a6,a7]
                            del(index[index.index(a5)])
                            if a5 in index:continue
                            for a6 in range(10):
                                index=[a0,a1,a2,a3,a4,a5,a6,a7]
                                del(index[index.index(a6)])
                                if a6 in index:continue
                                for a7 in range(10):
                                    index=[a0,a1,a2,a3,a4,a5,a6,a7]
                                    del(index[index.index(a7)])
                                    if a7 in index:continue
                                    val_lettres=[a0,a1,a2,a3,a4,a5,a6,a7]
                                    if tous_differents():
                                        calcul_operation()

    print (result)
    print ("END")



if __name__ == '__main__':
    a=['send','more','money']
    lettres=''
    val_lettres=[]
    #r=[0,0,0]
    num=[]
    found=0
    result=[]

    main()

