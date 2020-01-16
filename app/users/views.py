"""
    User views file
"""
from flask_restplus import Namespace, Resource, reqparse, fields
from flask import request
from app.users.models import Users, UsersSchema
from app.users.models import UsersSchema

API = Namespace('Users', description="User's RESTPlus - API")
USERS_SCHEMA = UsersSchema()


class UserAuth(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('user_id', required=True, type=str,
                        help="ID", location='json')
    parser.add_argument('id', required=True,
                        type=str, help="User's id", location='json')
    parser.add_argument('select', required=True,
                        type=str, help="number", location='json')
    user_login_field = API.model('signUp', {
        'id': fields.String,
        'user_id': fields.String,
        'number': fields.Integer,
    })
    def post(self):
        args = request.args
        print(args)
        return "test"


    def insert(self, args_):

        key = args_.get('aser').get('asdfe')
        value =args_.get('aser').get('asdfe')
        return "insert"


def insert(key, userId):
    user = Users(key, userId)
    result = user.add(user, USERS_SCHEMA)
    return result