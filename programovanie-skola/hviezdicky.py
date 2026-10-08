cislo = 0

def davajcislo():
    global cislo
    cislo = int(input("davaj cislo: "))
    print("tvoje cislo: "+ str(cislo))
    return cislo
    


while True:
    davajcislo()
    while cislo>0:
        print(str(cislo)+": "+"*"*cislo)
        cislo -= 1
