import random

slovo = ""
pismeno = ""
pismena = []
zobrazene = []
chyby = 0
vsetkyslova = [
    "bicykel",
    "program",
    "pocitac",
    "klavesnica",
    "monitor",
    "internet",
    "telefon",
    "programator",
    "fakulta",
    "hardver",
    "softver",
    "procesor",
    "prehliadac",
    "televizor",
    "baterka",
    "tabulka",
    "zostava",
    "stranka",
    "funkcia",
    "priklad"
]
sibenica = [
    """
       -----
       |   |
           |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
    ---------
    """
]
chyby = 0
zle = []
def vyber():
    global slovo,vsetkyslova
    slovo = random.choice(vsetkyslova)
    for i in range(len(slovo)):
        print("_")
        hadaj()
    return slovo , vsetkyslova

def hadaj():
    global slovo , pismeno,sibenica,pismena,chyby,zobrazene,zle
    print("//--------------------------//")
    pismeno = input("skus uhadnut pismeno: ")
    while len(pismeno) != 1:
        pismeno = input("musis zadat 1 pismeno: ")
    if pismeno in slovo:
        pismena.append(pismeno)
        print("uhadol si pismeno")
    else:
        print("neuhadol si")
        zle.append(pismeno)
        chyby += 1
    if chyby >7:
        print("prehral si")
        vyber()
    zobrazene = []
    for pismeno in slovo:
        if pismeno in pismena:
            zobrazene.append(pismeno)
        else:
            zobrazene.append("_")
    print(sibenica[chyby])
    print(" ".join(zobrazene))
    if "_" not in zobrazene:
        print("Gratulujem, vyhral si!")
        vyber()    
    print(f"nespravne pismena: {zle}")
    hadaj()
    return slovo , pismeno,sibenica, pismena,chyby,zobrazene,zle
    
vyber()



