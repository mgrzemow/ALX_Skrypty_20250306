"""
Ćwiczenie:

1. Użytkownik jest proszony o podanie imienia.
2. Tak długo jak użytkownik nie poda 'koniec' powtarzamy:
    2.1 wypisujemy 'Cześć Janek' gdzie Janek to podane imię.

Podpowiedzi:
 - pętla while
 - break

Rozszerzenia ćwiczenia:
 - jak uniknąć wielokrotnego użycia input?
 - jak uniknąć wielokrotnego użycia input oraz użycia break?

"""
# 1. wartość początkowa
# imie = None
# while imie != 'koniec':
#     if imie is not None:
#         print(f'Cześć {imie}')
#     imie = input('Podaj imie: ')

# 2.  wyjście przez break
# while True:
#     imie = input('Podaj imie: ')
#     if imie == 'koniec':
#         # jakiś dodatkowy kod
#         break
#     print(f'Cześć {imie}')

# 3. od 3.8 - operator walrus :=

# while (imie := input('Podaj imie: ')) != 'koniec':
#     print(f'Cześć {imie}')

r = 10
h = 10
v = (s := 3.14 * r * r) * h
print(f'Pole podstawy: {s}, objętość {v}')
