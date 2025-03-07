x = 'mama'
y = "mama"
print(x == y)
x = "<a href=\"http://onet.pl\">onet.pl</a>"
y = '<a href="http://onet.pl">onet.pl</a>'
print(x == y)
x = 'Tom\'s sick'
y = "Tom's sick"
print(x == y)

x = '''Linia 1
linia 2
linia 3
'''
y = 'Linia 1\nlinia 2\nlinia 3\n'
print(x == y)

p1 = 'C:\\dev\\PycharmProjects\\ALX_Skrypty_20250306\\c1.py'
open(p1)
# r - Raw - backslash jest zwykłym znakiem
p2 = r'C:\dev\PycharmProjects\ALX_Skrypty_20250306\c2.py'
open(p1)

# też często do wyrażeń regularnych
wr = '\\d\\d\\d'
wr1 = r'\d\d\d'

# co można zrobić z napisami - sklejanie

print('ma' + 'ta')

# powtarzanie
print(3 * 'ma')

# uwaga jak sobie zrobić krzywdę !!!
liczba = '12'
liczba2 = float(liczba * 3)
print(liczba2)

print('-' * 79)

# budowa napisów ze zmiennych
imie = 'Jan'
wiek = 34
waga = 77.12
wzrost = 187.123123123123123

s = imie + ' ma ' + str(wiek) + ' lat, waży ' + str(waga) + ' kg i ma ' + str(wzrost) + ' cm.'
print(s)
s = f'{imie} ma {wiek} lat, waży {waga} kg i ma {wzrost} cm.'
print(s)

s = f'{imie:12} ma {wiek:08d} lat, waży {waga:.0f} kg i ma {wzrost:12.2f} cm.'
print(s)

s_szablon = '{:12} ma {:08d} lat, waży {:.0f} kg i ma {:12.2f} cm.'
s = s_szablon.format(imie, wiek, waga, wzrost)
print(s)

# import requests
# url_szablon = 'https://api.nbp.pl/api/exchangerates/rates/a/{}/?format=json'
# waluta = 'usd'
# url = url_szablon.format(waluta)
# j = requests.get(url).json()
# print(j['rates'][0]['mid'])

# https://docs.python.org/3/library/string.html#formatspec
print('--\n'*10)
# slicing, zakresy, wycinanki
x = 'abcdefgh'
# indeksy dodatnie
print(x[0])
print(x[1])
print(x[7])

#indeksy ujemne - od końca
print(x[-1])
print(x[-2])
print(x[-8])

# zakresy abcdefgh
# bcd
print(x[1:4])
# można pomijać wartości
print(x[:4])
print(x[1:])

# ciekawe łączenia indeksów dodatnich i ujemnych
# ostatnie 3 elementy
print(x[-3:])
# wszystkie poza pierwszymi dwoma
print(x[2:])
# wszystkie poza ostatnimi 5:
print(x[:-5])
# odrzucić pierwsze 2 i ostatnie 2
print(x[2:-2])
# trzeci parametr - krok
print(x[1:-1:2])
# w praktyce najczęściej do odwracania napisu
print(x[::-1])
# slicing jest SUPER!!!
# metody stringowe
# wszystko się da!
# metody informacyjne
print('abc'.isalpha())
print('123'.isdigit())
print('abc123'.isalnum())
print('ABC'.isupper())
print('abc'.islower())
print('ala ma kota'.startswith('ala'))
print('ala ma kota'.endswith('kota'))
# uwaga - do sprawdzania czy coś jest w czymś - in !!!
# tak można ale po co:
print('ala ma kota'.find('a') != -1)
# bo można tak
print('a' in 'ala ma kota')
print('r' not in 'ala ma kota')

# zarządzanie wielkością znaków
print('ala'.upper())
print('ALA'.lower())
print('ala ma kota'.capitalize())
print('ala ma kota'.title())
print('ala ma Kota'.swapcase())

# justowanie - można ale po co
print('Tom'.center(10))
x = 'Tom'
print(f'{x:^10}')

# wypełnianie danymi
# więcej - doczytać
x = 'Ala'
y = 'Katowice'
print('{} mieszka w mieście {}'.format(x, y))

# wypisywanie napisów tak żeby dokładnie widzieć co jest w środku
x = 'Ala'
y = 'Ala\n'
print(x == y)
print(repr(x), repr(y))

# czyszczenie
x = 'Ala\n'
print(repr(x.strip()))
# dokładnie strip usuwa whitespace z początku i konca stringu
x = '  \t\n ala ma  kota\n\t '
print(repr(x.strip()))
print(repr(x.lstrip()))
print(repr(x.rstrip()))
# usuwanie przedrostków
x = 'BEGIN: sdasdasdasdasd as dasd sad as da a'
print(x.removeprefix('BEGIN: '))

# split
x = 'ala ma kota'
print(x.split(' '))
x = '  ala  ma \t kota\n'
print(x.split(' '))
# każdy cioąg whitespaceów jako pojedynczy separator
print(x.split())

x = ['ala', 'ma', 'kota']
print(' <-> '.join(x))

# niemutowalność
x = 'ala'
print(x)

# zamiana
x = 'mama'
print(x.replace('m', 'k'))

# jesteśmy w UTF8
print(hex(ord('ą')))

