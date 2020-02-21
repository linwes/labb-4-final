from random import randint
from flask import jsonify, Flask, request
import requests
import time

def skrivTill():
    while True:
        regn = randint(1,100)
        snö= randint(1,100)
        värme = randint(-30,40)
        data_dict = {'regn':regn, 'snö':snö, 'värme':värme}
        r = requests.post('http://127.0.0.1:5000/postjson', json=data_dict) 
        print(r.status_code)
        print(r.json())
        print(r.headers)
        time.sleep(5)
skrivTill()