import requests

w = 'Czesc'
requests.get('http://127.0.0.1:5000/przyjmij_wiadomosc/{}'.format(w))
