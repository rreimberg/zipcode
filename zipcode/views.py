# -*- coding: utf-8 -*-

import json
import re
import requests

from flask import Blueprint, current_app as app, jsonify, request
from werkzeug.exceptions import BadRequest

from zipcode import db
from zipcode.models import Zipcode

api = Blueprint('api', __name__)

headers = {'content-type': 'application/json'}


@api.route("/zipcode/", methods=["POST"])
def add_zipcode():
    """get the zip_code param, consult Postmon service and save data
    """

    zip_code = request.form['zip_code']

    if not re.match('[0-9]{8}$', zip_code):
        raise BadRequest('zip_code param should be composed by 8 numbers')

    response = requests.get('{0}/{1}'.format(app.config['POSTMON_URL'], zip_code))

    # check status_code 200 or 404
    if response.status_code == 404:
        raise BadRequest('The zip_code is unknown for Postmon database')

    data = json.loads(response.content)

    obj = Zipcode(
        zip_code=data['cep'],
        address=data['logradouro'],
        neighborhood=data['bairro'],
        state=data['estado'],
        city=data['cidade'],
    )

    db.session.add(obj)
    db.session.commit()

    return jsonify(obj), 201, headers


@api.route("/zipcode/", methods=["GET"])
def list_zipcode():
    """Return a list limited by limit request arg
    """

    query = Zipcode.query

    return json.dumps([dict(zipcode) for zipcode in query.all()]), 200, headers


@api.route("/zipcode/<zip_code>/", methods=["GET"])
def get_zipcode(zip_code):
    """Return a zip_code detail acording to specified param
    """

    obj = {
        'zip_code': '14020260',
        'address': 'Avenida Presidente Vargas',
        'neighborhood': 'Jd América',
        'state': 'SP',
        'city': 'Ribeirão Preto',
    }

    return jsonify(obj), 200, headers


@api.route("/zipcode/<zip_code>/", methods=["DELETE"])
def delete_zipcode(zip_code):
    """Delete zip_code record
    """
    return '', 204, headers
