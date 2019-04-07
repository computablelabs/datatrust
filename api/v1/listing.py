"""
Resource definition for Drive Listing
"""

from flask import request
from flask_restful import Resource, reqparse

class Listing(Resource):
    """
    Listing definition
    """
    def get(self):
        return {'listing': 'this is a listing'}

    def post(self):
        json_data = request.get_json(force=True)
        data = json_data
        if not json_data:
            return {'message': 'No input data provided'}, 400
        print(type(json_data))
        return f'You posted {data} with data'
