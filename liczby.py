# tyl stałoprzecinkowy - int - liczby całkowite
x = 12
print(type(x))
x = 1_233_222
print(x)

# to się wylicza w trakcie kompilacji
x = 24 * 60 * 60

x = 0b111
print(x)

x = 0xaa
print(x)

# float - liczby ułamkowe
x = 12.34
x = .123123
x = 12.
x = 1.3343e12
print(x)

print(1 + 1.5)
print(2 ** 3)

import math

print(math.sqrt(16))
print(math.sin(.1212))

print(abs(-12))

# dalsza matematyka -> numpy(macierze), scipy

# uwaga na zespolone
print((9) ** .5)
print((-9) ** .5)
# to się wywali na liczbie ujemnej
# print(math.sqrt(-16))
print(.1 + .2 == .3)
print(.1 + .2)

print(.1 + .2 == .3)
print(abs(.1 + .2 - .3) < .00001)
print(round(.1 + .2, 6)  == .3)
print(math.isclose(.1 + .2, .3))

# bardziej zaawansowane bibilioteki
# import fractions
# !!!
# import decimal

# konwersje
print(int('12'))
print(float('12'))
print(str(12.222))