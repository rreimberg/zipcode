# -*- coding: utf-8 -*-


from zipcode.config.base import Configuration as Base


class Configuration(Base):

    POSTMON_URL = 'http://postmon.url'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

    DEBUG = True
