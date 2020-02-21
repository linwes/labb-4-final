import sqlite3
from flask import Flask, escape, request, jsonify, render_template
from random import randint
import requests
import time
app = Flask(__name__)
conn = sqlite3.connect('blabla.db')
c = conn.cursor()
c.execute("""CREATE TABLE väder(
    regn text,
    snö text,
    värme text,
    dag interger  
    )""")
conn.commit()
conn.close()