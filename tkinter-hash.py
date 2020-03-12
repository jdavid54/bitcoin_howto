#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jean
#
# Created:     15/02/2018
# Copyright:   (c) Jean 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
from tkinter import messagebox
import hashlib


def affiche():
    global oktext
    #shaHash = hashlib.md5()
    algo=int(value.get())
    #protocol="MD5"
    if algo==1:
        shaHash = hashlib.md5()
        protocol="MD5"
    if algo==2:
        shaHash = hashlib.sha1()
        protocol="SHA1"
    if algo==3:
        shaHash = hashlib.sha256()
        protocol="SHA256"
    if algo==4:
        shaHash = hashlib.sha256()
        protocol="2xSHA256"
    if algo==5:
        shaHash = hashlib.sha512()
        protocol="SHA512"
    print(algo,protocol,oktext)

    if algo ==4:
        solution = hashlib.sha256(hashlib.sha256(oktext.encode('utf8')).digest()).hexdigest()    #double hash
    else:
        shaHash.update(oktext.encode('utf8'))
        solution = shaHash.hexdigest()
    text2.set(solution)

#GUI
fenetre = Tk()
columnsize=5
rowsize=8
can= Canvas(fenetre,height=50,width=900)   #il faut définir la taille du canvas en colonnes et rangées
can.grid(column=0,row=0,columnspan=columnsize,rowspan=rowsize)

#choix du protocole
"""
#bouton radio 1
vals = [1, 2, 3, 4]
etiqs = ['MD5', 'SHA1', 'SHA256', 'SHA512']
varGr = StringVar()
varGr.set(vals[1])
for i in range(4):
    b = Radiobutton(fenetre, variable=varGr, text=etiqs[i], value=vals[i])
    b.grid(column=i,row=7,columnspan=1,rowspan=1)
"""


pourquoitext=['suppression','ajout','perte de focus']
Ok=False
#zone texte à hasher
def estOK(pourquoi, quoi, result):      #result %P est la bonne chine après modif
    if Ok :
        global oktext
        print(pourquoitext[int(pourquoi)],entree.get()+"*"+quoi,result)
        oktext=result
        affiche()
    return True

okCommand=fenetre.register(estOK)
text1 = StringVar()
text1.set("texte par défaut")
entree = Entry(fenetre, textvariable=text1, width=100,validate='all',validatecommand=(okCommand, '%d','%S','%P'))     #%d pourquoi, %S quoi, %P oktext
#entree.pack()
entree.grid(column=0,row=2,columnspan=5,rowspan=1)
#zone texte réponse
text2 = StringVar()
text2.set("SHA1:")
entree2 = Entry(fenetre, textvariable=text2, width=130)
#entree2.pack()
entree2.grid(column=0,row=3,columnspan=5,rowspan=1)
Ok = True
oktext=entree.get()
#bouton radio 2
value = StringVar()
value.set(2)      # select bouton 2
bouton1 = Radiobutton(fenetre, text="MD5", variable=value, value=1,selectcolor='red',indicatoron=0,command=affiche)
bouton2 = Radiobutton(fenetre, text="SHA1", variable=value, value=2,selectcolor='red',indicatoron=0,command=affiche)
bouton3 = Radiobutton(fenetre, text="SHA256", variable=value, value=3,selectcolor='red',indicatoron=0,command=affiche)
bouton4 = Radiobutton(fenetre, text="2xSHA256", variable=value, value=4,selectcolor='red',indicatoron=0,command=affiche)
bouton5 = Radiobutton(fenetre, text="SHA512", variable=value, value=5,selectcolor='red',indicatoron=0,command=affiche)
bouton1.select()    # algo=md5 par défaut

#bouton1.pack(side='left', expand=1)
#bouton2.pack(side='left', expand=1)
#bouton3.pack(side='left', expand=1)
#bouton4.pack(side='left', expand=1)
bouton1.grid(column=0,row=0,columnspan=1,rowspan=1)
bouton2.grid(column=1,row=0,columnspan=1,rowspan=1)
bouton3.grid(column=2,row=0,columnspan=1,rowspan=1)
bouton4.grid(column=3,row=0,columnspan=1,rowspan=1)
bouton5.grid(column=4,row=0,columnspan=1,rowspan=1)
"""
#bouton calcul
bouton10=Button(fenetre, text="Calcul", command=affiche)
bouton10.grid(column=0,row=5,columnspan=2)      # si grid pas de pack
#bouton10.pack()
"""
#bouton fermer
bouton20=Button(fenetre, text="Fermer", command=fenetre.destroy)
bouton20.grid(column=2,row=5,columnspan=1)
#bouton20.pack()
"""
for c in range(4):
    bouton10=Button(fenetre, text="Calcul", command=affiche)
    bouton10.grid(column=c,row=7,columnspan=1)
"""


affiche()

def alert():
    messagebox.showinfo("alerte", "Bravo!")

menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Créer", command=alert)
menu1.add_command(label="Editer", command=alert)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.destroy)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Couper", command=alert)
menu2.add_command(label="Copier", command=alert)
menu2.add_command(label="Coller", command=alert)
menubar.add_cascade(label="Editer", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu=menubar)




mainloop()

def main():
    pass

if __name__ == '__main__':
    main()
