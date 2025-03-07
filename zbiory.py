# zbiory zapewniają unikalność elementów
# pusty
s = set()
# wypełniony - uwaga - kolejność jest losowa
s = {'ala', 'ola', 'kasia'}
print(s)
s.add('paweł')
print(s)
# dodanie drugi raz tego samego elementu
s.add('paweł')
print(s)
#  w praktyce - do usuwania duplikatów
x = [3, 2, 5, 2, 3, 'ola', 'ala', 'ula', 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 7, 7]
print(list(set(x)))
