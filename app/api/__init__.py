"""
    API config file
"""

from flask_restplus import Api
from app.users.views import API

REST_API = Api()
REST_API.add_namespace(API, '/user')