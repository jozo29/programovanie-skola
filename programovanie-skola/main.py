from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI()

sklad = {
    "jablko": {"cena": 0.5, "pocet": 200},
    "banan": {"cena": 0.8, "pocet": 600},
    "chlieb": {"cena": 1.5, "pocet": 120},
    "mlieko": {"cena": 2.0, "pocet": 300}
}
kosik = []

@app.get("/", response_class=HTMLResponse)
def zobraz_stranku():
    sklad_html = ""
    for nazov, data in sklad.items():
        sklad_html += f"<li><b>{nazov}</b> – Cena: {data['cena']} € | Na sklade: {data['pocet']} ks</li>"

    kosik_html = ""
    celkova_cena = 0
    for polozka in kosik:
        spolu = polozka['cena'] * polozka['pocet']
        celkova_cena += spolu
        kosik_html += f"<li>{polozka['nazov']} – {polozka['pocet']} ks x {polozka['cena']} € = {spolu} €</li>"

    return f"""
    <html>
        <head>
            <meta charset="utf-8">
            <title>jozov obchdo</title>
        </head>
        <body style="font-family: Arial; margin: 40px;">
            <h1>domoooov</h1>
            
            <h2> sklad:</h2>
            <ul>{sklad_html}</ul>

            <hr>

            <h2>1/pridac na sklad:</h2>
            <form action="/pridat-na-sklad" method="post">
                <label>nazov tovaru:</label><br>
                <input type="text" name="nazov" required><br><br>
                
                <label>Cena za kus (€):</label><br>
                <input type="number" step="0.01" name="cena" required><br><br>

                <label>pocet kusou:</label><br>
                <input type="number" name="pocet" required><br><br>
                
                <button type="submit">Uložiť na sklad</button>
            </form>

            <hr>

            <h2>2/kupic:</h2>
            <form action="/pridat-do-kosika" method="post">
                <label>nazov tovaru:</label><br>
                <input type="text" name="nazov" required><br><br>
                
                <label>pocet kusov:</label><br>
                <input type="number" name="pocet" required><br><br>
                
                <button type="submit">pridac do kosika</button>
            </form>

            <hr>

            <h2>tvoj kosik:</h2>
            <ul>{kosik_html}</ul>
            <h3>cena celeho nakupu: {celkova_cena} €</h3>
        </body>
    </html>
    """

@app.post("/pridat-na-sklad")
def pridat_na_sklad(nazov: str = Form(...), cena: float = Form(...), pocet: int = Form(...)):
    nazov_l = nazov.lower().strip()
    if nazov_l in sklad:
        sklad[nazov_l]["cena"] = cena
        sklad[nazov_l]["pocet"] += pocet
    else:
        sklad[nazov_l] = {"cena": cena, "pocet": pocet}
    
    return RedirectResponse(url="/", status_code=303)

@app.post("/pridat-do-kosika")
def pridat_do_kosika(nazov: str = Form(...), pocet: int = Form(...)):
    nazov_l = nazov.lower().strip()
    if nazov_l in sklad:
        cennik = sklad[nazov_l]["cena"]
        if sklad[nazov_l]["pocet"] >= pocet:
            kosik.append({"nazov": nazov_l, "cena": cennik, "pocet": pocet})
            sklad[nazov_l]["pocet"] -= pocet
            
    return RedirectResponse(url="/", status_code=303)