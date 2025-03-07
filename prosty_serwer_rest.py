import flask
app = flask.Flask(__name__)

# Jeżeli coś poważniejszego to raczej fastapi:
# https://fastapi.tiangolo.com/


@app.route('/dodaj/<x>/<y>')
def dodaj(x, y):
    return {'wynik': float(x) + float(y)}

@app.route('/przyjmij_wiadomosc/<w>')
def przyjmij_wiadomosc(w):
    print('przyjąłem wiadomość: ', w)
    return {'wynik': 'Przyjąłem'}

if __name__ == '__main__':
    app.run(debug=True)