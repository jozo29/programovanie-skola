from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# 1. Slovník tvojho skladu
sklad = {
    "jablko": {"cena": 0.5, "pocet": 200},
    "banan": {"cena": 0.8, "pocet": 600},
    "chlieb": {"cena": 1.5, "pocet": 120},
    "mlieko": {"cena": 2, "pocet": 300},
}


@app.get("/sklad")
def davajsklad():
    return sklad


@app.get("/kupit")
def kupit_produkt(produkt: str,mnozstvo: int = 1):
    if produkt not in sklad:
        return {"chyba": "Tento produkt v sklade neexistuje!"}
    
    if sklad[produkt]["pocet"] <= mnozstvo:
        return {"chyba": f"na sklade neni dost{produkt}!\nna sklade je {sklad[produkt]["pocet"]}"}
        
    sklad[produkt]["pocet"] -= mnozstvo
    return {
        "sprava": f"Úspešne kúpené: {mnozstvo}x {produkt}",
        "zostava_na_sklade": sklad[produkt]["pocet"]
    }


@app.get("/pridat")
def pridat_na_sklad(produkt: str, mnozstvo: int = 1):
    if produkt in sklad:
        sklad[produkt]["pocet"] += mnozstvo
    else:
        sklad[produkt] = {"cena": 1.0, "pocet": mnozstvo}
        
    return {
        "sprava": f"Úspešne pridané {mnozstvo}x {produkt} na sklad!",
        "aktualny_stav": sklad[produkt]
    }

@app.get("/", response_class=HTMLResponse)
def domov():
    with open("index.html", "r", encoding="utf-8") as subor:
        return subor.read()