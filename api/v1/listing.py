"""
Resource definition for Drive Listing
"""

from flask import request
from flask_restful import Resource, reqparse

class Listing(Resource):
    """
    Listing definition
    """
    def __init__(self, db):
        self.db = db

    def get(self):
        return {'listing': 'this is a listing'}

    def post(self):
        json_data = request.get_json(force=True)
        data = json_data
        if not json_data:
            return {'message': 'No input data provided'}, 400
        response = self.db.add_listing(json_data)
        if response == 'Success':
            return {'message': 'Success'}, 201
        elif response == 'Error writing to database':
            return {'message': 'Error writing to database'}, 500
        elif response == 'ValidationException':
            return {'message': 'Improper payload format'}, 400
        else:
            return {'message': 'Unknown status from database returned'}, 500
