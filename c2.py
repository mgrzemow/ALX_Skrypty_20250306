"""
Ćwiczenie:

Napisać program, który:
 1. Wczyta z konsoli kwotę brutto i stawkę VAT
 2. Wypisze kwotę netto i kwotę VAT wg podanej stawki

 Podpowiedzi:
 - input() zwraca zawsze obiekt str (napis) - konieczna jest konwersja do typów liczbowych

 Rozszerzenia ćwiczenia:
 - wczytać z konsoli i zamienić na liczbę w jednej linii

"""
brutto = input('Podaj kwotę brutto: ')
brutto = float(brutto)

stawka = float(input('Podaj stawkę VAT: '))
netto = round(brutto / (1 + stawka / 100), 2)
vat = round(brutto - netto, 2)
print('Kwota netto: ', netto)
print('Kwota VAT: ', vat)
