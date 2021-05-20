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
    return render_template("inicio.html")
