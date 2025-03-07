"""
Ćwiczenie:

 1. Wczytać z konsoli:
  - nazwę tagu XML/HTML,
  - nazwę atrybutu,
  - wartość tagu
  - wartość atrybutu
 2. Skonstruować na tej podstawie kawałek XMLa/HTMLa.

 Np. dla danych a, href, onet, http://onet.pl
 Wypisać: <a href = "http://onet.pl">onet</a>

 Podpowiedzi:
  - f-strings
"""

if __name__ == '__main__':
    tag = input('Podaj nazwę tagu: ')
    atrybut = input('Podaj nazwę atrybutu: ')
    tag_w = input('Podaj zawartość tagu: ')
    atrybut_w = input('Podaj wartość atrybutu: ')
    print(f'<{tag} {atrybut}="{atrybut_w}">{tag_w}</{tag}>')
