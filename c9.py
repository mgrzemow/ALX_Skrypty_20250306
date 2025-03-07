"""
Ćwiczenie:

Napisać program, który:

1. Wczyta napis z konsoli:
2. Policzy ilość liter i ilość cyfr w napisie.

Podpowiedzi:
 - pętla for dla napisów iteruje po znakach
 - '8'.isdigit() == True
 - 'a'.isalpha() == True
"""
if __name__ == '__main__':
    napis = input('Podaj napis: ')
    ilosc_cyfr = 0
    ilosc_liter = 0
    ilosc_alfanumerykow = 0
    for znak in napis:
        if znak.isdigit():
            ilosc_cyfr += 1
        if znak.isalpha():
            ilosc_liter += 1
        if znak.isalnum():
            ilosc_alfanumerykow += 1
    print(f'Ilosc liter: {ilosc_liter}, ilosc cyfr: {ilosc_cyfr}, ilosc alfanumerykow: {ilosc_alfanumerykow}')