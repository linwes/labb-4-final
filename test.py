import sqlite3
import requests
from flask import Flask, render_template, jsonify, request
from random import randint
import time

app = Flask(__name__)
  
@app.route('/postjson', methods=['POST'])

def postJsonHandler():
    print(f'request.is_json: {request.is_json}')
    content=request.get_json()
    print(f'content: {content}') 
    con = sqlite3.connect('väder.db')
    c = con.cursor()
    g = (content['regn'], content['snö'], content['värme'])
    c.execute("INSERT INTO väder (regn, snö, värme) VALUES (?,?,?)",g)
    con.commit()
    con.close()
    return '{"message":"JSON post success"}'
app.run(host='127.0.0.1', port=5000)