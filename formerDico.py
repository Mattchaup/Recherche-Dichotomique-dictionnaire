def ecrirDico(name,liste):
    with open(name,"w",encoding="utf-8") as doss:
        for mot in liste:
            for info in mot[:28]:
                doss.write(info+"&")
            doss.write("\n")
    return "done"

def openDoc(name):
    dico=[]
    with open (name, 'r',encoding="utf-8") as doss:
        lmots = doss.readlines()
    for mot in lmots:
        dico.append(mot[0:-1].lower())
    return dico

def openTextDoc(name):
    listeMot = []
    with open (name, 'r',encoding="utf-8") as doss:
        lmots = doss.readlines()

    for ligne in lmots:
        listeMot += splitSentence(ligne.lower())
        
    return listeMot

def openCsvDoc(name,sp):
    allWord = []
    with open(name,'r',encoding="utf-8") as doss:
        lmots = doss.readlines()
    
    for mot in lmots:
        allWord.append(mot[:-1].split(sp))
    return allWord

def findWeirdLette(dico):
    for mot in dico:
        for l in mot[0]:
            if l not in letter:
               print(mot[0])

def findWords(phrase,listeMots):
    mot = ""
    for index,char in enumerate(phrase):
        if char not in letter:
            if mot != "":
                listeMots.append(mot)
            return findWords(phrase[index+1:],listeMots)
        else:
            mot += char
    return listeMots

def splitSentence(phrase):
    listeMot = []
    mot = ""
    for lettre in phrase:
        if lettre in separateur:
            if mot != "":
                listeMot.append(mot)
                mot = ""
        else:
            mot += lettre
    return listeMot

def afficherDicoto(liste):
    if len(liste) > 0:
        long = len(liste) // 2
        #print(liste[long])
        listeTriee.append(liste[long])
        del liste[long]
        afficherDicoto(liste[:long])
        afficherDicoto(liste[long:])

letter = [" ","-","'",".","a","b","c","d","e","f","g","h","i","j","k",
"l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","à","â","ã",
"ç","é","è","ê","ë","î","ï","ñ","ô","ö","ù","û","ü"]

separateur = [" ","’","-",".",",","!","?",";",":","'","…"]

#--------------------------------------
#--------------- Main -----------------
#--------------------------------------

#l = openTextDoc("texte.txt")
listeMot = []


"""
listeTriee = []
dicoOrdonee = openCsvDoc("Lexique/Lexique383.tsv","\t")
findWeirdLette(dicoOrdonee)
print(len(dicoOrdonee))
afficherDicoto(dicoOrdonee[1:])
print(listeTriee[0])
ecrirDico("tomiDico.txt",listeTriee)
"""