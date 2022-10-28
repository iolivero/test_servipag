#!/usr/bin/env python
import json
from flask import Flask, Response

app = Flask(__name__)
@app.route('/personas', methods=['GET'])
def index():
    payload = [{
        'id': 1,
        'nombres': 'Pedro',
        'apellido_paterno': 'Torres',
        'apellido_materno': 'Acuña',
        'email': 'ptorresa@servipag.cl'
    },
    {
        'id': 2,
        'nombres': 'Ana',
        'apellido_paterno': 'Lara',
        'apellido_materno': 'Araya',
        'email': 'alaray@servipag.cl'
    },
    {
        'id': 3,
        'nombres': 'Daniela Andrea',
        'apellido_paterno': 'Camacho',
        'apellido_materno': 'Valdivia',
        'email': 'ptorresa@servipag.cl'
    } ]
    return Response(json.dumps(payload), mimetype='application/json')
app.run(host='0.0.0.0', port=5000)
