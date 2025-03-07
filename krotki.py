# Krotki (tuple) czyli nie mutowalne listy
k = (1, 2, 3)

# W 99% przypadków można zamiast krotek używać list !!!

# Czasem się zdarzy że jakaś funkcja oczekuje krotki:
x = [1,2,3]
k = tuple(x)
print(k)
x1 = list(k)
print(x1)

# Jeden szczególny przypadek - krotka jednoelementowa:
k = (1)
print(type(k), k)

k = (1,)
print(type(k), k)
