import sqlite3
from flask import Flask, escape, request, jsonify, render_template

conn = sqlite3.connect('databass.db')

app = Flask(__name__)

@app.route("/")
def start():
    return render_template('index.html')

@app.route('/', methods=['post'])
def skrivUt():
    användare = [request.form.get('fNamn'),
    request.form.get('efterNamn'),
    request.form.get('address'),
    request.form.get('postNummer'),
    request.form.get('ort'),
    request.form.get('Nummer'),
    request.form.get('ePost'),
    request.form.get('losenord'),
    request.form.get('betala'),
    request.form.get('erbjudande'),
    request.form.get('format'),
    request.form.get('kommentar'),]
    
    fNamn = användare[0]
    efterNamn = användare[1]
    address = användare[2]
    postnummer = användare[3]
    stad = användare[4]
    nummer = användare[5]
    ePost = användare[6]
    lösen = användare[7]
    betala = användare[8]
    erbjudande = användare[9]
    eFormat = användare[10]
    kommentar = användare[11]
    return render_template('index.html', fNamn=fNamn, efterNamn=efterNamn, address=address, postNummer=postnummer, ort=stad, nummer=nummer, ePost=ePost, losenord=lösen, betla=betala, erbjudande=erbjudande, format=eFormat, kommentar=kommentar)

if __name__ :
    app.debug = True
    app.run(host= '127.0.0.1', port=5000)