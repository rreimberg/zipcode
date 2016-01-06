# -*- coding: utf-8 -*-

import json

from .base import BaseTestCase


class ApiTestCase(BaseTestCase):

    def test_add_zipcode_successful(self):

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

    def test_list_zipcode_successful(self):

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

    def test_delete_zipcode_successful(self):

        response = self.client.delete('/zipcode/14020260/')

        self.assertEqual(204, response.status_code)
        self.assertEqual('application/json', response.content_type)

        self.assertEqual('', response.data)

    def test_get_zipcode_successful(self):

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
