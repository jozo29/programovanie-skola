sklad = {"jablko":{"cena":0.5,
                   "pocet":200},
        "banan":{"cena":0.8,
                 "pocet":600},
        "chlieb":{"cena":1.5,
                  "pocet":120},
        "mlieko":{"cena":2,
                  "pocet":300}
   }
while True:
    print("co chces spravit?\n1 = pridat na sklad\n2 = kupit")
    menu = input()
    while menu != "1" and menu != "2":
        print("musis zadat cislo 1 alebo 2")
        menu = input()
    menu = int(menu)
    if menu == 1:
        print("co chces pridat na kosik? ")
        item = input()
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
            testpocet = input(f"kolko kusov chces chces pridat na sklad z polozky {item}?")
            if testpocet.isdigit():
                pocet = int(testpocet)
                break
            else:
                print("musis zadat pocet cislom")
        sklad[item] = {"cena": cena,
                    "pocet":pocet}
        print("sklad bol aktualizovany")
        for i in sklad:
            print(i)
    





    