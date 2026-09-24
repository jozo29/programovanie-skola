zoznam = []
celacena = 0
while True:
    item = input("co chces pridat na zoznam? ")
    if item.lower() == "nic":
        break
    while True:
        testcena = input(f"kolko sotji jeden kus z polozky: {item}?")
        try: 
            cena = float(testcena)
            break
        except ValueError:
            print("musis zadat cislo aby sa dala vypoctac cena")
    while True:
        testpocet = input(f"kolko kusov chces kupit z polozky {item}?")
        if testpocet.isdigit():
            pocet = int(testpocet)
            break
        else:
            print("musis zadat pocet cislom")
    zoznam.append({
        "polozka": item,
        "cena za kus": cena,
        "pocet kusov": pocet
    })
    celacena += cena*pocet
    print("\n//------tvoj nakupny kosik------//")
    print("")
    for i in zoznam:
        print(i)
    print("")
    print(f"cena celeho nakupu:       {celacena}")
    print("//------------------------------//")
    