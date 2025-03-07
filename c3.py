"""
Ćwiczenie:

 1. Wczytać z konsoli nr roku
 2. Sprawdzić czy rok jest przestępny.
 3. Wypisać odpowiedni komunikat

 Podpowiedzi:
    Rok jest przestępny jeżeli spełniony jest chociaż jeden z dwóch warunków:
    - dzieli się przez 400
    lub
    - dzieli się przez 4 i nie dzieli się przez 100

 Rozszerzenia ćwiczenia:
  - nie użyć w kodzie ani jednego dwukropka ':'
  - sprawdzić czy użytkownik podał całkowitą liczbę dodatnią > 0
"""

rok = int(input('Podaj rok: '))

if rok < 0:
    print('nr roku ma być dodatni')
    exit()

# if rok % 400 == 0 or rok % 4 == 0 and rok % 100 != 0:
#     print('rok przestępony')
# else:
#     print('rok nie przestępny')

dzieli_4 = rok % 4 == 0
dzieli_100 = rok % 100 == 0
dzieli_400 = rok % 400 == 0
czy_przestepny = dzieli_400 or dzieli_4 and not dzieli_100
komunikat = 'rok przestępny' if czy_przestepny else 'rok nie przestępny'

print(komunikat)
