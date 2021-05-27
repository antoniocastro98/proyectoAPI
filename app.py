from flask import Flask, abort, render_template, request
import requests
import json
import os
URL_BASE="https://futdb.app/"
key=os.getenv("key")
cabeceras={"accept": "application/json","X-AUTH-TOKEN":key}
app = Flask (__name__)

@app.route('/',methods=["GET"])
def inicio():
    return render_template("inicio.html")

@app.route('/ligas', methods=["GET"])
def ligas():
    ligas=request.form.get(URL_BASE+'api/leagues', headers=headers)
    if request.method=="GET":
        return render_template("ligas.html")   
    else:
        cabeceras={"accept": "application/json","X-AUTH-TOKEN":key"}
        r=requests.post(URL_BASE+"api/players",headers=cabeceras)	
        if r.status_code==200:
            lista=[]
            for i in datosjugador["items"]:
            lista.append(i)
        return render_template('ligas.html', ligas1=ligas1)




@app.route('/jugadores/',methods=["GET","POST"])
def jugadores():
    jugadores1=request.form.get("jugador")
    if request.method=="GET":
        return render_template("jugadores.html")    
    else: 
            cabeceras={"accept": "application/json","X-AUTH-TOKEN":key,"Content-Type": "application/json"}
            datos="{\"name\":\"%s\"}" %jugadores1
            r=requests.post(URL_BASE+"api/players",headers=cabeceras,data=datos)	
            if r.status_code==200:
                datosjugador=r.json()
                lista=[]
                for i in datosjugador["items"]:
                    lista.append(i)
                print(i)
                id=datosjugador.get("items")[0].get("id")

            return render_template("jugadores.html",datos=lista,id=id)	

 

@app.route('/cartas')
def cartas():
        return render_template("cartas.html")





app.run(debug=True)
