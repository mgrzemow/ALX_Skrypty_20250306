# pusty słownik
d = {}
# już wypełniony
d = {'Ania': 34,
     'Ola': 34,
     'Paweł': 23}

print(d)
print(d['Ola'])
# jak nie wiadomo o co chodzi to chodzio klucze
print(34 in d)
print('Ola' in d)
for klucz in d:
    print(klucz)

# kluczami mogą być liczby
{1: 'jeden',
 2: 'dwa',
 3: 'trzy',
 5: 'pięć'}

# oraz wszystko to co niemutowalne
{
    ('Ania', 'Kowalska') : [...]
}

d = {'Ania': 34,
     'Ola': 34,
     'Paweł': 23}

# dodawanie
d['Ula'] = 25
# nadpisywanie
d['Ola'] = 55

print(d)

# usuwanie:
del(d['Ania'])
print(d)
