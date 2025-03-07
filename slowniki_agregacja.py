x = 'mama tata mama mama tata ja'

wynik = {'mama': 3, 'tata': 2, 'ja': 1}

d = {}
for slowo in x.split():
    if slowo not in d:
        d[slowo] = 1
    else:
        d[slowo] = d[slowo] + 1

print(d)

# w pisaniu bardziej skrótowego kodu pomoże: .get .setdefault i collections.defaultdict

