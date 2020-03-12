# coding: utf-8
import hashlib
import pickle

block ={
    'transactions':[
        {
            'from' : 'A',
            'to' : 'B',
            'amount' : 10
        },
        {
            'from' : 'B',
            'to' : 'C',
            'amount' : 10
        },
        {
            'from' : 'C',
            'to' : 'D',
            'amount' : 10,
            'message' : 'thanks for the help!'
        },
    ]
}

print(block)

pickle.dumps(block)
m = hashlib.sha3_256()
m.update(pickle.dumps(block))
m.digest()
m.hexdigest()
#bloc modifié
block2 ={
    'transactions':[
        {
            'from' : 'A',
            'to' : 'B',
            'amount' : 1000000      #augmentation de la valeur
        },
        {
            'from' : 'B',
            'to' : 'C',
            'amount' : 10
        },
        {
            'from' : 'C',
            'to' : 'D',
            'amount' : 10,
            'message' : 'thanks for the help!'
        },
    ]
}
n = hashlib.sha3_256()
n.update(pickle.dumps(block2))
n.hexdigest()
#différence de hash
print(m.hexdigest())
print(n.hexdigest())

#Considérons un bloc valide
top_block ={
    'transactions':[
        {
            'from' : 'A',
            'to' : 'B',
            'amount' : 10
        },
        {
            'from' : 'B',
            'to' : 'C',
            'amount' : 10
        },
        {
            'from' : 'C',
            'to' : 'D',
            'amount' : 10,
            'message' : 'thanks for the help!'
        },
    ],
    'last_block' : m.hexdigest(),
    'nonce' : 0
}
print(top_block)
#on va créer et valider un bloc avec une valeur de difficulté
o = hashlib.sha3_256()
o.update(pickle.dumps(top_block))
print(o.hexdigest())
# le mining c'est rechercher une valeur pour nonce qui permet de résoudre la difficulté
#ici pour la difficulté x, c'est d'obtenir x zéros en tête dans le hash
difficulty = 6
difficulty_string = ''.join(['0' for x in range(difficulty)])
print(difficulty_string)

#opération de mining
# on part avec une valeur de nonce (ici 1) et on incrémente de 1 et à chaque fois on l'injecte dans le bloc
# puis on refais le calcul du hash jusqu'à l'obtention du hash avec la condition

def mine():
    nonce = 11320000
    top_block['nonce']=1
    p = hashlib.sha3_256()
    while p.hexdigest()[:difficulty] != difficulty_string:
        nonce += 1                        #on incrémente nonce
        top_block['nonce'] = nonce        #on injecte dans le bloc
        p = hashlib.sha3_256()
        p.update(pickle.dumps(top_block))
        if nonce%10000==0:print(nonce)
        #print(nonce, p.hexdigest())
    #on a gagné
    print(nonce, p.hexdigest())

import timeit
t=timeit.Timer("mine()","from __main__ import mine").timeit(1)
print(t)