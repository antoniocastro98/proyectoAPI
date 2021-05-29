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
        cabeceras={"accept": "application/json","X-AUTH-TOKEN":key,"Content-Type": "application/json"}
        r=requests.post(URL_BASE+"api/leagues",headers=cabeceras)	
        if r.status_code==200:
            ligas1=r.json()
            lista=[]
            for i in ligas1["items"]:
                lista.append(i)
        return render_template('ligas.html', ligas1=lista)





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
                ritmo=datosjugador.get("items")[0].get("pace")
                pase=datosjugador.get("items")[0].get("passing")
                disparo=datosjugador.get("items")[0].get("shooting")
                fisico=datosjugador.get("items")[0].get("physicality") 
                regate=datosjugador.get("items")[0].get("dribbling") 
                defensa=datosjugador.get("items")[0].get("defending")
                id1=datosjugador.get("items")[0].get("id") 
                return render_template("jugadores.html" ,id1=id1, ritmo=ritmo,pase=pase,disparo=disparo,fisico=fisico,regate=regate,defensa=defensa)	


@app.route('/precios', methods=["GET"])
def precios():
    jugadores1=request.form.get("jugador")    
    if request.method=="GET":
        return render_template("precios.html")   
    else:
        cabeceras={"accept": "application/json","X-AUTH-TOKEN":key,"Content-Type": "application/json"}
        datos="{\"name\":\"%s\"}" %jugadores1
        r=requests.post(URL_BASE+"api/players",headers=cabeceras,data=datos)
        if r.status_code==200:
            jugadores=r.json()
            id2=jugadores.get("items")[0].get("id")
        r2=requests.post(URL_BASE+"/api/players/%s/price",headers=cabeceras) %id2
        if r2.status_code==200:
            precios=r.json()

        return render_template('precios.html', precios=lista2,id=id2)



app.run(debug=True)
