from flask import Flask, abort, render_template, request
import requests
import json
import os
app = Flask (__name__)
URL_BASE="https://futdb.app/"
key=os.getenv("key")
cabeceras={"accept": "application/json","X-AUTH-TOKEN":key}


@app.route('/',methods=["GET"])
def inicio():
    return render_template("inicio.html")

@app.route('/ligas', methods=["GET"])
def ligas():
        cabeceras={"accept": "application/json","X-AUTH-TOKEN":key}
        r=requests.get(URL_BASE+"api/leagues",headers=cabeceras)	
        ligas1=r.json()
        ligaid1=ligas1.get("items")[3].get("id")
        liganom1=ligas1.get("items")[3].get("name")
        ligaid2=ligas1.get("items")[5].get("id")
        liganom2=ligas1.get("items")[5].get("name")
        ligaid3=ligas1.get("items")[7].get("id")
        liganom3=ligas1.get("items")[7].get("name")
        ligaid4=ligas1.get("items")[9].get("id")
        liganom4=ligas1.get("items")[9].get("name")
        ligaid5=ligas1.get("items")[14].get("id")
        liganom5=ligas1.get("items")[14].get("name")
        return render_template('ligas.html', ligaid1=ligaid1 , liganom1=liganom1 , ligaid2=ligaid2 , liganom2=liganom2 , ligaid3=ligaid3 , liganom3=liganom3, ligaid4=ligaid4 , liganom4=liganom4, ligaid5=ligaid5 , liganom5=liganom5)

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
            nombre= datosjugador.get("items")[0].get("common_name") 
            return render_template("jugadores.html",id1=id1,ritmo=ritmo,pase=pase,disparo=disparo,fisico=fisico,regate=regate,defensa=defensa,nombre=nombre)
        else:
            return abort(404)


@app.route('/precios/', methods=["GET","POST"])
def precios():
    jugadores2=request.form.get("jugadorp")    
    if request.method=="GET":
        return render_template("precios.html")   
    else:
        cabeceras={"accept": "application/json","X-AUTH-TOKEN":key,"Content-Type": "application/json"}
        datos="{\"name\":\"%s\"}" %jugadores2
        r=requests.post(URL_BASE+"api/players",headers=cabeceras,data=datos)
        if r.status_code==200:
            jugadores=r.json()
            id2=jugadores.get("items")[0].get("id")
            nombre=jugadores.get("items")[0].get("common_name")
            id3=str(id2)
            print(id3)
            print(type(id3))
            r2=requests.post(URL_BASE+"api/players/"+id3+"/price",headers=cabeceras)
            if r2.status_code==200:
                precios=r2.json()
                xbox=precios.get("xbox").get("price") 
                ps4=precios.get("playstation").get("price")
                pc=precios.get("pc").get("price") 
                return render_template('precios.html',id=id2,xbox=xbox,pc=pc,ps4=ps4,nombre=nombre)
        else:
            return abort(404)


port=os.environ["PORT"]
app.run('0.0.0.0', int(port), debug=True)