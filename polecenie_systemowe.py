# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "requests",
#     "typer",
# ]
# ///

import typer
import requests

URL_SZABLON_MID = 'https://api.nbp.pl/api/exchangerates/rates/a/usd/?format=json'
URL_SZABLON_ASK = 'https://api.nbp.pl/api/exchangerates/rates/c/usd/?format=json'

app = typer.Typer()


@app.command()
def pobierz_kurs(waluta: str) -> float:
    url = URL_SZABLON_MID.format(waluta)
    j = requests.get(url).json()
    print(j['rates'][0]['mid'])

@app.command()
def wylicz_kwote(kwota: float, waluta: str, kurs_sredni:bool=True) -> float:
    if kurs_sredni:
        url = URL_SZABLON_MID.format(waluta)
        klucz = 'mid'
    else:
        url = URL_SZABLON_ASK.format(waluta)
        klucz = 'ask'

    j = requests.get(url).json()
    print(j['rates'][0][klucz] * kwota)

if __name__ == '__main__':
    app()
