"""
Resource definition for Drive Listing
"""

from flask import request
from flask_restful import Resource

class Listing(Resource):
    """
    Listing definition
    """
    def __init__(self, db):
        self.db = db

    def get(self):
        json_data = request.get_json(force=True)
        data = json_data
        if not json_data:
            return {'message': 'No input data provided'}, 400
        response = self.db.get_listing(json_data)
        if response == 'Error retrieving record':
            return {'message': 'Error retrieving record'}, 500
        else:
            return response, 200

    def post(self):
        json_data = request.get_json(force=True)
        data = json_data
        if not json_data:
            return {'message': 'No input data provided'}, 400
        response = self.db.add_listing(json_data)
        print(response)
        if response == 'Success':
            return {'message': 'Success'}, 201
        elif response == 'Error writing to database':
            return {'message': 'Error writing to database'}, 500
        elif response == 'ValidationException':
            return {'message': 'Improper payload format'}, 400
        else:
            return {'message': response}, 500

    def delete(self):
        json_data = request.get_json(force=True)
        data = json_data
        if not json_data:
            return {'message': 'No input data provided'}
        response = self.db.delete_listing(json_data)
        if response == 'Error deleting record':
            return {'message': response }, 500
        else:
            return {'message': response}, 200
