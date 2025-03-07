"""
Ćwiczenie:

Napisać program, który:

1. Będzie sprawdzał w pętli while czy istnieje plik 'lock.txt'
2. Tak długo jak plik istnieje będzie:
 - wypisywał komunikat: 'Plik lock.txt istnieje, usuń go aby kontynuować. Masz N s'
 - zmniejszał ilość pozostałych sekund o 1 (zaczynamy odliczanie od powiedzmy 15.
3. Po usunięciu pliku 'lock.txt' w wyznaczonym czasie wypisze 'No, nareszcie! Musiałem cię poganiać {n} razy'
4. Jeżeli pozostały czas dobiegnie końca, wypisze 'Za późno, żegnam'

Podpowiedzi:
 - import os.path
   os.path.isfile()
 - import time
   time.sleep()
"""
import os.path
import time

if __name__ == '__main__':
    n = 15
    m = 15
    while True:
        if not os.path.isfile('lock.txt'):
            print(f'No, nareszcie! Musiałem cię poganiać {m-n} razy')
            break
        if n < 1:
            print('Za późno, żegnam')
            break
        print(f'Plik lock.txt istnieje, usuń go aby kontynuować. Masz {n} s')
        n -= 1
        time.sleep(1)
