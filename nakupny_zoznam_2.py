kosik = []
celacena = 0
while True:
    print("//------------------------//")
    print("zadaj co chces zrobic: \n1 = pridat do kosika\n2 = zobrat z kosika\n3 = zmenit pocet\n4 = zmenit cenu\n5 = koniec\n6 = vytlacit nakupny kosik")
   
    while True:
        menu = input("napis sem:")
        try:
            menu = int(menu)
            break
        except ValueError:
            print("musis zadat cislo od 1 do 5 a tym vyberies co chces spravit") 
        
    if menu == 1:
        vec = input("zadaj co chces pridat do kosika: ")
        while True:
            cena = input(f"napis kolko stoji jeden kus polozky {vec}: ")
            try:
                cena = float(cena)
                break
            except ValueError:
                print("musis zadat cislom cenu")
        while True:
            pocet = input(f"zadaj pocet kuov ktore chces kupit z polozky {vec}: ")
            try:
                pocet = int(pocet)
                break
            except ValueError:
                print("muisi zadar cele cislo")
        kosik.append({
            "polozka": vec,
            "ceana za 1 kus": cena,
            "pocet kusov": pocet
        })
        celacena += pocet * cena
        print("tvoj nakupny kosik: ")
        for i in kosik:
            print(i)
        print("")
        print(f"cena celeho nakupu: {celacena}$")
    elif menu == 2: