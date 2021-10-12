def openDoc(name):
    dico=[]
    with open (name, 'r',encoding="utf-8") as doss:
        lmots=doss.readlines()
    for mot in lmots:
        dico.append(mot[0:-1].lower())
    return dico

def findNoobWord(dico,mot):
    for m in dico:
        if m == mot:
            return "trouvé avec la méthode naïve"

scoreLetter = {" ":0,"-":1,"'":2,".":3,"a":4,"b":5,"c":6,"d":7,"e":8,"f":9,"g":10,"h":11,"i":12,"j":13,"k":14,
"l":15,"m":16,"n":17,"o":18,"p":19,"q":20,"r":21,"s":22,"t":23,"u":24,"v":25,"w":26,"x":27,"y":28,"z":29,"à":30,
"â":31,"ã":32,"ç":33,"é":34,"è":35,"ê":36,"ë":37,"î":38,"ï":39,"ñ":40,"ô":41,"ö":42,"ù":43,"û":44,"ü":45}

class Word:
    def __init__(self,infos):
        while len(infos)<28:
            infos.append(0)
        self.apparition = 1
        self.motstr = infos[0]
        self.index = [scoreLetter[lettre] for lettre in infos[0]]
        self.phono = infos[1]
        self.lemme = infos[2]
        self.cgram = infos[3]
        self.genre = infos[4]
        self.nombre = infos[5]
        self.freqlemfilms = infos[6]
        self.freqlemlivres = infos[7]
        self.freqfilms = infos[8]
        self.freqlivres = infos[9]
        self.infover = infos[10]
        self.nbhomogr = infos[11]
        self.nbhhomoph = infos[12]
        self.islem = infos[13]
        self.nblettres = infos[14]
        self.nbphon = infos[15]
        self.cvcv = infos[16]
        self.p_cvcv = infos[17]
        self.voisorth = infos[18]
        self.voisphon = infos[19]
        self.puorth = infos[20]
        self.puphon = infos[21]
        self.syll = infos[22]
        self.nbsyll = infos[23]
        self.cv_cv = infos[24]
        self.orthrenv = infos[25]
        self.phonrenv = infos[26]
        self.orthosyll = infos[27]

    
    def __str__(self):
        return self.motstr

class Node:
    def __init__(self,info,left,right):
        self.info = info
        self.left = left
        self.right = right

class dicoTree:
    def __init__(self):
        self.root = None
    
    def fillWord(self,mot): #directement dans la class avec la liste d'index
        if self.root == None:
            self.root = Node(mot,None,None)
        else:
            current = self.root
            parent = None
            gene = None
            i = 0

            while current != None:
                parent = current
                if mot.motstr == current.info.motstr:
                    current.info.apparition += 1
                    return
                if i >= len(mot.motstr):
                    current = current.left
                    i = 0
                    gene = "gauche"
                elif i >= len(current.info.motstr):
                    current = current.right
                    i = 0
                    gene = "droite"
                elif mot.index[i] > current.info.index[i]:
                    current = current.right
                    i = 0
                    gene = "droite"
                elif mot.index[i] < current.info.index[i]:
                    current = current.left
                    i = 0
                    gene = "gauche"
                else:
                    i += 1
            
            current = Node(mot,None,None)
            if gene == "gauche":
                parent.left = current
            elif gene == "droite":
                parent.right = current
            else:
                print("bip boup erreur")
    
    def bestWord(self):
        if self.root == None:
            return "Le classement est vide"
        return dicoTree.findBest(self.root,None)
    
    @staticmethod
    def findBest(r,parent):
        if r.right != None:
            return dicoTree.findBest(r.right,r)
        return r,parent
    
    def findWord(self,mot):
        if self.root == None:
            return "erreur"
        else:
            return dicoTree.trouverMot(self.root,mot)
    
    @staticmethod
    def trouverMot(current,mot):
        i = 0
        while current.info.motstr != mot.motstr:
            if i >= len(current.info.motstr):
                current = current.right
                i = 0
            elif i >= len(mot.motstr):
                current = current.left
                i = 0
            elif mot.index[i] > current.info.index[i]:
                current = current.right
                i = 0
            elif mot.index[i] < current.info.index[i]:
                current = current.left
                i = 0
            else:
                i += 1
            if current == None:
                return None
        return current