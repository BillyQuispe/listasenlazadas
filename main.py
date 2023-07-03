#!/usr/bin/env python
from flask import Flask
from flask import jsonify
from linkextractor import extrae

app = Flask(__name__)

@app.route("/")
def index():
    return "Usage: https://listasenlazadasapi.bjrcode.com [:<prt>]/api/<id>"

@app.route("/api/<int:id>")
def api(id):
    return jsonify(extrae(id))

app.run(host="0.0.0.0")
