zoznam = []
celacena = 0
gorie = []
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
    kateg = input(f"v akej kategorii je polozka {item}? ")
    if kateg not in gorie:
        gorie.append(kateg)
    zoznam.append({
        "polozka": item,
        "cena za kus": cena,
        "pocet kusov": pocet,
        "kategoria": kateg
    })
    celacena += cena*pocet
    print("\n//------tvoj nakupny kosik------//")
    print("")
    for i in zoznam:
        print(f"-{i["polozka"]}  cena: {i["cena za kus"]}$  {i["pocet kusov"]}x  kategoria: {i["kategoria"]}")
    print("")
    for i in gorie:
        print(f"{i}:\n")
        for p in zoznam:
            if p["kategoria"] == i:
                print(f"{p["polozka"]}")
    print("")
    print(f"cena celeho nakupu:       {celacena}$")
    print("//------------------------------//")
    