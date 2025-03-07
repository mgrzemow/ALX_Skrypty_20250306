"""
Z pliku teksotowego w formacie:
Ania 34
Ola 33
Paweł 44

1. Wczytać listę w formacie:

[
['Ania', 34],
...
]

2. Za pomocą tej listy wypisać komumikaty dla wszystkich osób:
Ania - 34

"""
from pprint import pprint


def wczytaj_osoby(nazwa_pliku: str = 'osoby.txt') -> list[tuple[str, int]]:
    with open(nazwa_pliku, 'rt', encoding='utf-8') as f:
        lista_rekordow = []
        for linia in f:
            imie, wiek = linia.split()
            wiek = int(wiek)
            rekord = [imie, wiek]
            lista_rekordow.append(rekord)
    return lista_rekordow


def wypisz_osoby(lista_rekordow: list[tuple[str, int]]) -> None:
    for imie, wiek in lista_rekordow:
        print(f'{imie} - {wiek}')


if __name__ == '__main__':
    lista_rekordow = wczytaj_osoby()
    # pprint(lista_rekordow)
    wypisz_osoby(lista_rekordow)
