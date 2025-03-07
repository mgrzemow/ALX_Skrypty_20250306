with open('tmp.txt', 'rt', encoding='utf-8') as f:
    print(f)
    print(f.read())

with open('tmp.txt', 'rt', encoding='utf-8') as f:
    for linia in f:
        print(repr(linia))
        print(linia.strip())

with open('tmp.txt', 'wt', encoding='utf-8') as f:
    f.write('linia1\n')
    f.write('linia2\n')
    f.write('linia3\n')
    print(f.closed)

print(f.closed)
''.split