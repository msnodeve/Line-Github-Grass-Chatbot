"""
    Create db
"""
from flask import jsonify
from flask import make_response
from http import HTTPStatus
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_marshmallow import Marshmallow

DB = SQLAlchemy()
MA = Marshmallow()


class CRUD:

    def add(self, resource, schema):
        try:
            DB.session.add(resource)
            result = DB.session.commit()
        except IntegrityError as err:
            DB.session.rollback()
        return result
