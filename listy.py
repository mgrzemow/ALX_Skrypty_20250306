x = ['ala', 0, None, 2.5]
print(0 in x)
print(1 in x)
for element in x:
    print(element)
print(x[:2])
x.append(12)
print(x)
x.append([13, 14])
print(x)
del (x[-1])
print(x)
x.extend([13, 14])
print(x)
x += [15, 16]
print(x)

# Lista użyta jako lista takich samuch elementów
lista_imion = ['Ala', 'Ola', 'Kazik']
for imie in lista_imion:
    print(imie)

# Lista jako rekord
rekord = ['Ola', 34, 167, 'Kraków']
miasto = rekord[3]

# Lista rekordów
lista_rekordow = [
    ['Ola', 34, 167, 'Kraków'],
    ['Ula', 34, 165, 'Kraków'],
    ['Jarek', 44, 167, 'Łódź'],
]

for rekord in lista_rekordow:
    print(f'{rekord[0]} mieszka w {rekord[3]}')

