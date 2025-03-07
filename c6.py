"""
Ćwiczenie:

Napisać program, który:

1. Na podstawie:
 - roku urodenia,
 - miesiąca urodzenia
 - dnia urodzenia
 - nr kolejnego
 - określenia płci True == mężczyzna

wygeneruje pesel w następującego schematu:
 - 2 ostatnie cyfry roku
 - 2 cyfrowy miesiąc uzupełniony od lewej zerem (jeżeli rok >= 2000 to do miesiąca dodajemy 20)
 - 2 cyfrowy dzień uzupełniony od lewej zerem
 - 3 cyfrowy nr kolejny uzupełniony od lewej zerem
 - cyfra płci - 1 mężczyzna, 0 kobieta
 - suma kontrolna będąca ostatnią cyfrą sumy powyższych cyfr

Np dla kobiety urodzonej 3.12.2005r jako 13ta osoba powinno wyjść:
05320301307

Podpowiedzi:
 - pętla for dla napisów iteruje po literach
 - str(12)
 - int('12')
 - '2'.zfill(3)
 - f'{2:03d}'
Rozszerzenia ćwiczenia:
 - czy da się uniknąć użycia zfill (formatowanie fstringów)
"""
if __name__ == '__main__':
    rok = 2002
    miesiac = 11
    dzien = 3
    nr = 34
    plec_facet = True
    
    # rok_s = str(rok)[-2:]
    # od roku 2000 dodajemy 20 do miesiący
    # if rok >= 2000:
    #     miesiac += 20
    
    # miesiac_s = str(miesiac).zfill(2)
    # dzien_s = f'{dzien:02d}'
    # nr_s = f'{nr:03d}'
    # plec_s = f'{int(plec_facet)}'
    # pesel = f'{rok_s}{miesiac_s}{dzien_s}{nr_s}{plec_s}'
    pesel = f'{str(rok)[-2:]}{miesiac + 20 if rok >= 2000 else miesiac:02d}{dzien:02d}{nr:03d}{(int(plec_facet))}'

    # wyliczyć sumę cyfr
    # suma = 0
    # for znak in pesel:
    #     suma += int(znak)
    # # dokleić
    # pesel += str(suma)[-1]
    
    pesel += str(sum(int(znak) for znak in pesel))[-1]
    print(pesel)