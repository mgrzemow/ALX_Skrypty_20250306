import json
import requests

url = 'https://api.nbp.pl/api/exchangerates/rates/a/usd/?format=json'

if __name__ == '__main__':
    # wysłanie zapytania
    r = requests.get(url)
    # kontrola status code
    print(r.status_code)
    # idzie dalej jeżeli ok, lub wyrzuca wyjątek
    r.raise_for_status()
    print(r)
    print(r.content)
    print(r.text)
    # to też może się nie udać
    j = r.json()
    kurs = j['rates'][0]['mid']
    print(kurs)
    with open('kurs.json', 'wt', encoding='utf-8') as f:
        json.dump(j, f, ensure_ascii=False, indent=2)
    s = json.dumps(j, ensure_ascii=False, indent=2)
    print(s)
    j1 = json.loads(s)
    print(j1['rates'][0]['mid'])
    with open('kurs.json', 'rt', encoding='utf-8') as f:
        j2 = json.load(f)
    print(j2['rates'][0]['mid'])
