# -*- coding: utf-8 -*-

from zipcode import db


class Zipcode(db.Model):

    zip_code = db.Column(db.String(8), primary_key=True)

    address = db.Column(db.String(512))
    neighborhood = db.Column(db.String(128))
    state = db.Column(db.String(50))
    city = db.Column(db.String(2))

    def __iter__(self):

        yield 'zip_code', self.zip_code
        yield 'address', self.address
        yield 'neighborhood', self.neighborhood
        yield 'state', self.state
        yield 'city', self.city
