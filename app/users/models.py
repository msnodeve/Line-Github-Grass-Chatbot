"""
    Users models file
"""
from marshmallow import fields, validate
from sqlalchemy.sql import text

from app.api.database import DB, MA, CRUD


class Users(DB.Model, CRUD):
    __tablename__ = 'users'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = DB.Column(DB.Integer, primary_key=True)
    user_id = DB.Column(DB.String(255), unique=True, nullable=False)
    created = DB.Column(DB.TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), nullable=False)

    def __init__(self,id: str, user_id: str):
        self.user_id = user_id


class UsersSchema(MA.Schema):
    not_blank = validate.Length(min=1, error='Field cannot be blank')
    id = fields.Integer(dump_only=True)
    user_id = fields.String(validate=not_blank)
    created = fields.String(validate=not_blank)
