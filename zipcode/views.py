# -*- coding: utf-8 -*-

import json

from flask import Blueprint, jsonify

api = Blueprint('api', __name__)

headers = {'content-type': 'application/json'}


@api.route("/zipcode/", methods=["POST"])
def add_zipcode():
    """get the zip_code param, consult api.postmon.com.br/v1/cep/14020260
    and save data"""

    obj = {
        'zip_code': '14020260',
        'address': 'Avenida Presidente Vargas',
        'neighborhood': 'Jd América',
        'state': 'SP',
        'city': 'Ribeirão Preto',
    }

    return jsonify(obj), 201, headers


@api.route("/zipcode/", methods=["GET"])
def list_zipcode():
    """Return a list limited by limit request arg
    """

    obj = [
        {
            'zip_code': '14020260',
            'address': 'Avenida Presidente Vargas',
            'neighborhood': 'Jd América',
            'state': 'SP',
            'city': 'Ribeirão Preto',
        }
    ]

    return json.dumps(obj), 200, headers


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
