import re
import subprocess
import datetime as dt
from pprint import pprint

wr = r'^(\d\d/\d\d/\d\d\d\d  \d\d:\d\d (AM|PM))\s+(\d+) (\S.*)$'
wrc = re.compile(wr)
r = subprocess.run('dir /-C',
                   shell=True,
                   capture_output=True,
                   encoding='cp1252')
# wyprodukować listę rekordów:
# [
#     ('c1.py', 344, <datetime>)
# ]
lista_rekordow = []
for linia in r.stdout.splitlines():
    m = wrc.match(linia)
    if m:
        d, _, wielkosc, nazwa = m.groups()
        wielkosc = int(wielkosc)
        d = dt.datetime.strptime(d, '%m/%d/%Y  %I:%M %p')
        lista_rekordow.append((nazwa, wielkosc, d))

pprint(lista_rekordow)
