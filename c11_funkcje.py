'''
Ćwiczenie:

Z pliku tekstowego w formacie:
Jan 888999777
Ola 333444555
Paweł 111222333
Ula 333444000

wczytac słownik w postaci:
{'Jan': '888999777',
 ...
}

Następnie napisać pętlę w której użytkownik będzie podawał imiona
a program będzie podawał numery telefonów, lub komunikat, że nie ma takiego numeru
w książce telefonicznej. Warunkiem wyjścia z pętli będzie podanie 'koniec' zamiast imienia.

Podpowiedzi:
 - kod ma pycharm

Wygodne narzędzie do generowania dokumentacji - pdoc3
'''

from c11_config import PLIK_TELEFONY

def wczytaj_dane(nazwa_pliku: str = PLIK_TELEFONY) -> dict[str, str]:
    """
    Funkcja czytująca książkę telefoniczną.

    Dalszy opis:
    - format danych wejściowych
    - reakcja na błędy
    - opis parametrów wejściowych
    - itd

    Do doczytania -
    google: 'python docstrings' 'python docstring formats'
    type hinting:
    https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html

    Args:
        nazwa_pliku: oipsa nazwa pliku

    Returns:

        **słownik z wynikami**

    """

    with open(nazwa_pliku, 'rt', encoding='utf-8') as f:
        ksiazka_tel = {}
        for linia in f:
            imie, tel = linia.split()
            ksiazka_tel[imie.lower()] = tel
    return ksiazka_tel


if __name__ == '__main__':
    ksiazka_tel = wczytaj_dane()
    x = ksiazka_tel['ala']


    while (imie := input('Podaj imie: ')) != 'koniec':
        imie = imie.lower()
        if imie in ksiazka_tel:
            print(f'Nr do: {imie.capitalize()}: {ksiazka_tel[imie]}')
        else:
            print(f'Nie mam nr do: {imie.capitalize()}')
