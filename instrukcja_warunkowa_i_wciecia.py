# if 2 == 2:
#     print('pod ifem 1')
#     print('pod ifem 2')
#     print('pod ifem 3')
#     print('pod ifem 4')
#     if 3 == 3:
#         print('pod zagnieżdżonym ifem')
# elif 2 == 3:
#     print('elif 1')
#     print('elif 2')
#     print('elif 3')
# else:
#     print('else 1')
#     print('else 2')
#     print('else 3')
# 
# print('poza ifem')
import math
from _ast import Not

x = ''
# dla napisów - czy nie pusty
if x:
    print('x is true')
else:
    print('x is false')

x = 0
# dla liczb - czy nie zero
if x:
    print('x is true')
else:
    print('x is false')

x = []
x = [1, 2, 3]
# dla sekwencji - czy nie pusty
if x:
    print('x is true')
else:
    print('x is false')

# jeżeli nie jest liczbą ani nie da się wyliczyć długości
import datetime as dt
x = dt.datetime.now()
t = None
if t:
    print('x is true')
else:
    print('x is false')

# częsty schemat
import re
w = re.match('t', 'mama')
if w:
    print('Jest dopasowanie: ', w)
else:
    print('Nie ma dopasowania: ', w)