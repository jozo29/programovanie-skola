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
    print("co chces spravit?\n1 = pridat na sklad\n2 = kupic\nkonec = konec")
    menu = input()
    
    
    if menu == "1":
        print("co chces pridat na sklad? ")
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
        print("<===>")
        print("sklad bol aktualizovany")
        print("<===>")
        c = 1
        for a,s in sklad.items():
            
            print(f"{c}. - {a}\n     {s["cena"]}$\n     {s["pocet"]}ks")
            c += 1
    elif menu == "2":
        print("co chces kupic?")
        item = input()
        while item not in sklad:
            print("mozes kupic lenb daco co je na sklade")
            print("na zozname je len toto:")
            for i in sklad.items():
                print("  ",i)
            print("co teda chces kupic?")
            item = input()
        print(f"na sklade je: {sklad[item]["pocet"]} kusov z polozky {item}")
        while True:
            print(f"kolko {item} chces kupic?")
            pocet = input()
            if pocet.isdigit():
                pocet = int(pocet)
                if pocet > sklad[item]["pocet"]:
                    print(f"musis zadat cislo mensie asko {sklad[item]["pocet"]+1}")
                else:
                    break
            else:
                print("musis zadat cislo")
        sklad[item]["pocet"] -= pocet
        print("<===>")
        print("sklad bol aktualizovany")
        print("<===>")
        c = 1
        for a,s in sklad.items():
            print(f"{c}. - {a}\n     {s["cena"]}$\n     {s["pocet"]}ks")
            c += 1
        print("<===>")
    elif menu == "konec":
        print("dakujem za vas nakup, skllad sa zatvara")
        break
    else:
        print("musis zadac bud 1,2 alebo konec ty neamdertalec")

                
        
                     
           