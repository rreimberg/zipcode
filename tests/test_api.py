# -*- coding: utf-8 -*-

import httpretty
import json

from .base import BaseTestCase

from zipcode import db
from zipcode.models import Zipcode


class ApiTestCase(BaseTestCase):

    @httpretty.activate
    def test_add_zipcode_successful(self):

        postmon_response = """
{"complemento": "at\\u00e9 489 - lado \\u00edmpar",
"bairro": "Jd Am\\u00e9rica",
"cidade": "Ribeir\\u00e3o Preto",
"logradouro": "Avenida Presidente Vargas",
"estado_info": {"area_km2": "248.222,362", "codigo_ibge": "35",
"nome": "S\\u00e3o Paulo"},
"cep": "14020260", "cidade_info":
{"area_km2": "650,955", "codigo_ibge": "3543402"}, "estado": "SP"}
        """

        httpretty.register_uri(httpretty.GET, 'http://postmon.url/14020260',
                               body=postmon_response)

        expected = {
            u'zip_code': u'14020260',
            u'address': u'Avenida Presidente Vargas',
            u'neighborhood': u'Jd América',
            u'state': u'SP',
            u'city': u'Ribeirão Preto',
        }

        response = self.client.post('/zipcode/', data={'zip_code': 14020260})

        self.assertEqual(201, response.status_code)
        self.assertEqual('application/json', response.content_type)
        data = json.loads(response.data)

        self.assertEqual(expected, data)

    def test_add_zipcode_without_param_code(self):

        response = self.client.post('/zipcode/')
        self.assertEqual(400, response.status_code)

        response = self.client.post('/zipcode/', data={'zip_code': ''})
        self.assertEqual(400, response.status_code)

    def test_add_zipcode_with_invalid_code(self):

        response = self.client.post('/zipcode/', data={'zip_code': '14020-260'})
        self.assertEqual(400, response.status_code)

        response = self.client.post('/zipcode/', data={'zip_code': 'adsffdsag'})
        self.assertEqual(400, response.status_code)

    @httpretty.activate
    def test_add_zipcode_with_unknown_code(self):

        httpretty.register_uri(httpretty.GET, 'http://postmon.url/14020260',
                               body='', status=404)

        response = self.client.post('/zipcode/', data={'zip_code': 14020260})

        self.assertEqual(400, response.status_code)

    def test_list_zipcode_successful(self):

        # get a empty list
        response = self.client.get('/zipcode/')

        self.assertEqual(200, response.status_code)
        self.assertEqual('application/json', response.content_type)
        self.assertEqual('[]', response.data)

        zipcode = Zipcode(
            zip_code=u'14020260',
            address=u'Avenida Presidente Vargas',
            neighborhood=u'Jd América',
            state=u'SP',
            city=u'Ribeirão Preto',
        )
        db.session.add(zipcode)

        expected = [{
            u'zip_code': u'14020260',
            u'address': u'Avenida Presidente Vargas',
            u'neighborhood': u'Jd América',
            u'state': u'SP',
            u'city': u'Ribeirão Preto',
        }]

        response = self.client.get('/zipcode/')

        self.assertEqual(200, response.status_code)
        self.assertEqual('application/json', response.content_type)
        data = json.loads(response.data)

        self.assertEqual(expected, data)

    def test_list_zipcode_with_limit(self):

        zipcode1 = Zipcode(
            zip_code=u'14020260',
            address=u'Avenida Presidente Vargas',
            neighborhood=u'Jd América',
            state=u'SP',
            city=u'Ribeirão Preto',
        )

        zipcode2 = Zipcode(
            zip_code=u'14020261',
            address=u'Avenida Presidente',
            neighborhood=u'Jd América',
            state=u'SP',
            city=u'Ribeirão Preto',
        )

        zipcode3 = Zipcode(
            zip_code=u'14020263',
            address=u'Avenida Vargas',
            neighborhood=u'Jd América',
            state=u'SP',
            city=u'Ribeirão Preto',
        )

        db.session.add(zipcode1)
        db.session.add(zipcode2)
        db.session.add(zipcode3)

        response = self.client.get('/zipcode/?limit=asd')
        self.assertEqual(400, response.status_code)

        response = self.client.get('/zipcode/?limit=-1')
        self.assertEqual(400, response.status_code)

        response = self.client.get('/zipcode/?limit=0')
        self.assertEqual(200, response.status_code)
        self.assertEqual('[]', response.data)

        response = self.client.get('/zipcode/?limit=2')
        self.assertEqual(200, response.status_code)
        data = json.loads(response.data)

        self.assertEqual(2, len(data))

        response = self.client.get('/zipcode/?limit=5')
        self.assertEqual(200, response.status_code)
        data = json.loads(response.data)

        self.assertEqual(3, len(data))

        response = self.client.get('/zipcode/?limit=')
        self.assertEqual(200, response.status_code)
        data = json.loads(response.data)

        self.assertEqual(3, len(data))

        response = self.client.get('/zipcode/')
        self.assertEqual(200, response.status_code)
        data = json.loads(response.data)

        self.assertEqual(3, len(data))

    def test_delete_zipcode_successful(self):

        zipcode = Zipcode(
            zip_code=u'14020260',
            address=u'Avenida Presidente Vargas',
            neighborhood=u'Jd América',
            state=u'SP',
            city=u'Ribeirão Preto',
        )
        db.session.add(zipcode)

        response = self.client.delete('/zipcode/14020260/')

        self.assertEqual(204, response.status_code)
        self.assertEqual('', response.data)

        self.assertEqual(0, Zipcode.query.count())
        n_zipcode = Zipcode.query.filter_by(zip_code='14020260').first()

        self.assertIsNone(n_zipcode)

    def test_delete_zipcode_with_non_existent_code(self):

        response = self.client.delete('/zipcode/14020260/')
        self.assertEqual(404, response.status_code)

    def test_get_zipcode_successful(self):

        zipcode = Zipcode(
            zip_code=u'14020260',
            address=u'Avenida Presidente Vargas',
            neighborhood=u'Jd América',
            state=u'SP',
            city=u'Ribeirão Preto',
        )
        db.session.add(zipcode)

        expected = {
            u'zip_code': u'14020260',
            u'address': u'Avenida Presidente Vargas',
            u'neighborhood': u'Jd América',
            u'state': u'SP',
            u'city': u'Ribeirão Preto',
        }

        response = self.client.get('/zipcode/14020260/')

        self.assertEqual(200, response.status_code)
        self.assertEqual('application/json', response.content_type)
        data = json.loads(response.data)

        self.assertEqual(expected, data)

    def test_get_zipcode_with_non_existent_code(self):

        response = self.client.get('/zipcode/14020260/')
        self.assertEqual(404, response.status_code)
