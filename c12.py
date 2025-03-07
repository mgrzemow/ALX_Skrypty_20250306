# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "requests",
#     "typer",
# ]
# ///
# napisać funkcję, która:
# 1. Będzie pobierać kurs poda nej waluty
# 2. Będzie przeliczać kwotę przez kurs i wypisywać wartość

"""
uv:
https://github.com/astral-sh/uv
1. Zainstalować.
pip install uv, lub inaczej
2. Dodanie nagłówka do skryptu:
uv add --active --script c12.py typer requests
3. Uruchomienie skryptu:
uv run c12.py

Pyinstaller:
1. pip install pyinstaller
2. pyinstaller -F c12.py
-F - generuje exe
3. No i mamy execa.

"""

import typer
import requests

URL_SZABLON_MID = 'https://api.nbp.pl/api/exchangerates/rates/a/{}/?format=json'
URL_SZABLON_ASK = 'https://api.nbp.pl/api/exchangerates/rates/c/{}/?format=json'

app = typer.Typer()

@app.command()
def wylicz_kwote(kwota: float, waluta: str, kurs_sredni: bool = True) -> float:
    """
    Calculates the converted amount.

    Calculates the converted amount based on the given currency and exchange rate
    type (average or ask rate). The function fetches live currency rates from a
    specified URL template, multiplies the fetched rate by the inputted amount,
    and prints the resulting converted amount.

    Args:
        kwota: The monetary amount to be converted.
        waluta: The currency code (e.g., 'USD', 'EUR') for the exchange rate.
        kurs_sredni: Indicates whether an average rate ('mid') or ask rate ('ask')
            should be used for the conversion. Defaults to True (average rate).

    Returns:
        float: The converted monetary amount after applying the chosen currency exchange rate.

    """
    if kurs_sredni:
        url = URL_SZABLON_MID.format(waluta)
        klucz = 'mid'
    else:
        url = URL_SZABLON_ASK.format(waluta)
        klucz = 'ask'

    j = requests.get(url).json()
    print(j['rates'][0][klucz] * kwota)
    return j['rates'][0][klucz] * kwota

if __name__ == '__main__':
    app()