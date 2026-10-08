

nakupnykosik = []

while True:
    print("co chces kupic")
    novapolozka = input()
    if novapolozka == "hotovo" or novapolozka == "nic":
        break
    else:
        nakupnykosik.append(novapolozka) 
        print(f"v kosiku mas: {nakupnykosik}")



    