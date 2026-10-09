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
        <body style="font-family: Arial, sans-serif; margin: 40px;">
            <h1>domoooov</h1>
            
            <h2> sklad:</h2>
            <ul>{sklad_html}</ul>

            <hr>

            

            <h2>KUPIC:</h2>
            <form action="/pridat-do-kosika" method="post">
                <label>nazov tovaru:</label><br>
                <input type="text" name="nazov" required><br><br>
                
                <label>pocet kusov:</label><br>
                <input type="number" name="pocet" required><br><br>
                
                <button type="submit" style = "color: green;">pridac do kosika</button>
            </form>

            <hr>

            <h2>tvoj kosik:</h2>
            <ul>{kosik_html}</ul>
            <h3>cena celeho nakupu: {celkova_cena} €</h3>

            <hr>

            <p><a href="/admin">prejst na rezim admin</a></p>
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

@app.get("/admin", response_class=HTMLResponse)
def zobraz_admin():
    sklad_admin_html = ""
    for nazov, data in sklad.items():
        sklad_admin_html += f"<li><b>{nazov}</b> – Cena: {data['cena']} € | Počet: {data['pocet']} ks</li>"

    return f"""
    <html>
        <head><meta charset="utf-8"><title>Admin Panel</title></head>
        <body style="font-family: Arial, sans-serif; margin: 40px;">
            <h1>Administrácia skladu</h1>
            <p><a href="/">naspak domov</a></p>
            
            <h2>Aktuálny sklad:</h2>
            <ul>{sklad_admin_html}</ul>

            <h2>pridac alebo upravic na skolad:</h2>
            <form action="/pridat-na-sklad" method="post">
                <input type="text" name="nazov" placeholder="nazov tovaru" required><br><br>
                <input type="number" step="0.01" name="cena" placeholder="cena za kus" required><br><br>
                <input type="number" name="pocet" placeholder="pocet kusov" required><br><br>
                <button type="submit" style="color: green;">ulozit na sklad</button>
            </form>

            <h2>Odstrániť tovar zo skladu:</h2>
            <form action="/vymazat-zo-skladu" method="post">
                <input type="text" name="nazov" placeholder="tovcar kery chces vymazac" required><br><br>
                <button type="submit" style="color: red;">vymazac</button>
            </form>
        </body>
    </html>
    """

@app.post("/vymazat-zo-skladu")
def vymazat_zo_skladu(nazov: str = Form(...)):
    nazov_l = nazov.lower().strip()
    if nazov_l in sklad:
        del sklad[nazov_l]  # Vymaže položku zo slovníka
    
    return RedirectResponse(url="/admin", status_code=303)