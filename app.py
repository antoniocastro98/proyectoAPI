from flask import Flask, abort, render_template, request
import requests
import json
import os
URL_BASE="https://futdb.app/"
key=os.getenv("key")
cabeceras={"accept": "application/json","X-AUTH-TOKEN":key}
app = Flask (__name__)

@app.route('/')
def inicio():
    return render_template("/inicio.html")

@app.route('/ligas', methods=["GET"])
def ligas():
    r=requests.get(URL_BASE+"api/leagues",headers=cabeceras)
    if r.status_code == 200:
        datos=r.json()
        print(datos)

@app.route('/jugadores')
def jugadores():
    cabeceras={"accept": "application/json","X-AUTH-TOKEN":key,"Content-Type": "application/json"}
    datos="{\"name\":\"Cristiano Ronaldo\"}"
    r=requests.post(URL_BASE+"api/players",headers=cabeceras,data=datos)

    if r.status_code==200:
        datos=r.json()
        print(datos)
    else:
        datos=r.json()
        print(datos)

#como funciona las repsuestas de las peticiones en la app

port=os.environ["PORT"]

app.run('0.0.0.0', int(port), debug=False)
