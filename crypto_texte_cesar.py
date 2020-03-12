# -*- coding: utf-8 -*-
# crypto_texte_cesar créé par Jean le 01/08/2017
# Sujet :
# Le code César avec clé
# amélioré pour quelques erreurs (début par décodage, sortie par bouton Annuler)
#-------------------------------------------------------------------------------

from __future__ import division
import easyguifr as eg
import sys

debug=False
debug=True       #uncomment to debug

# u devant la chaîne pour Unicode
alphabet=u" ABCDEFGHIJKLMNOPQRSTUVWXYZ\
abcdefghijklmnopqrstuvwxyz0123456789\
.,:;!?&àâéèêëîïù#'(-_){}[]|\@=+°§$<>%*/"

long_Al=len(alphabet)
clef='FRED'
phrase='Bonjour ami'
phrasecode=''
quitte=False

def ord(ch):
    """
    #remplace la fonction ord classique
    """
    k=alphabet.find(ch)
    if k==-1:k=0
    return k

def chr(n):
    """
    #remplace la fonction chr classique
    """
    if n<0 or n>long_Al:n=0
    return alphabet[n]

def code_cesar(sa, L, coder):
    """
    Codage/décodage de la chaîne sa avec la clé L;
    La fonction renvoie la chaîne sp.
    La variable coder dit s'il faut coder (coder=True) ou décoder (coder=False)
    """
    z=len(L); u=0; sp=''
    while u<len(sa):
        if coder:
            m=ord(sa[u])+ord(L[u % z])
            m=m % long_Al
            if debug:print (m,sa[u],ord(sa[u]),L[u % z],ord(L[u % z]))
        else:
             m=ord(sa[u])-ord(L[u % z])
             m=m % long_Al
             if debug:print (m,sa[u],ord(sa[u]),L[u % z],ord(L[u % z]))
        sp=sp+chr(m)
        u=u+1
    return sp

while not quitte:
    resultat=eg.boite_bouton(msg="Sélectionner une action",titre="Instructions",choix=("Coder","Décoder","Quitter"))
    if resultat=="Quitter":
        quitte=True
    else:
        coder = resultat=="Coder"
        if coder:
            try :
                phrase, clef=eg.multsaisie_base( \
                msg="Complètez les valeurs de chaque champ" \
                , titre="Codage César" \
                , champs=['texte à coder', 'clef'] \
                , valeurs=[phrase,clef])
                sb = code_cesar(phrase,clef,coder)
            except:
                sys.exit(u"Programme annulé")  #si appui sur Annuler
        else:
            try:
                phrasecode, clef=eg.multsaisie_base( \
                msg="Complètez les valeurs de chaque champ" \
                , titre="Codage César" \
                , champs=['texte à décoder', 'clef'] \
                , valeurs=[phrasecode,clef])
                sb = code_cesar(phrasecode,clef,coder)
            except:
                sys.exit(u"Programme annulé")

        print(sb)
        if coder: phrasecode=sb
        else: phrase=sb

print (u"Programme terminé")