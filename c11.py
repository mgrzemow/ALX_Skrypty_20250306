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
'''

if __name__ == '__main__':
    with open('telefony.txt', 'rt', encoding='utf-8') as f:
        ksiazka_tel = {}
        for linia in f:
            imie, tel = linia.split()
            ksiazka_tel[imie.lower()] = tel
    print(ksiazka_tel)
    
    while (imie := input('Podaj imie: ')) != 'koniec':
        imie = imie.lower()
        if imie in ksiazka_tel:
            print(f'Nr do: {imie.capitalize()}: {ksiazka_tel[imie]}')
        else:
            print(f'Nie mam nr do: {imie.capitalize()}')
