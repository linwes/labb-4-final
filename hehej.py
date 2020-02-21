import requests
import sqlite3
from flask import Flask, escape, request, jsonify, render_template
from random import randint
app = Flask(__name__)

@app.route('/')
def skrivUt():
    conn = sqlite3.connect('väder.db')
    c = conn.cursor()
    c.execute("SELECT regn FROM väder")
    value = c.fetchall()
    s = " "
    for v in value:
        s = s+v[0] + "%, "
        
    c.execute("SELECT snö FROM väder")
    valuey = c.fetchall()
    t = " "
    for v in valuey:
        t = t+v[0] + "%, "
    
    c.execute("SELECT värme FROM väder")
    values = c.fetchall()
    u = " "
    for v in values:
        u = u+v[0] + ", "
    
    return render_template('väder.html', rain=s, snow=t, heat=u)

if __name__ :
    app.debug = True
    app.run(host= '127.0.0.1', port=5080)