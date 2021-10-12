#Import
from ArbreDeMot import*
from formerDico import openCsvDoc, openTextDoc
import time

#Ouverture du document texte
start = time.time()
dico = openCsvDoc("tomiDico.txt","&")
end = time.time()
duration = round(end-start,3)
print(f"Ouverture Dico : {duration} s")

#-------------------------------------------
motMystere = openTextDoc("texte.txt")

#----- Création du le l'arbre -----#
start = time.time()
dicopti = dicoTree()
for m in dico:
    dicopti.fillWord(Word(m))
end = time.time()
duration = round(end-start,3)
print(f"Trier Dico : {duration} s")

#----- Activité de recherche de mot (optionnel) -----#
phrase = "Text prononcé : "
start = time.time()
for mot in motMystere:
    motTrouve = (dicopti.findWord(Word([mot])))
    if motTrouve:
        phrase += motTrouve.info.phono + " "
    else:
        phrase += mot + " "
end = time.time()
duration1 = round(end-start,5)

#-------------------------------------------
print("\n~~~~~~~~ Résultat ~~~~~~~~ ")
print(f"Arbre : {duration1} s")
print(f"~~~~ Analyse du texte ~~~~")
print(phrase)