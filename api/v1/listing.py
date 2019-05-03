"""
Resource definition for Drive Listing
"""

from flask import request
from flask_restful import Resource
from flask_restful_swagger import swagger

class Listing(Resource):
    """
    Listing definition
    """
    def __init__(self, db):
        self.db = db

    @swagger.operation(
        notes='Retrieve a listing by listing hash',
        parameters=[
            {
                "name": "listing",
                "description": "The listing hash to retrieve",
                "required": True,
                "paramType": "body"
            }
        ],
        responseMessages=[
            {
                "code": 200,
                "message": "Listing returned to client"
            },
            {
                "code": 400,
                "message": "No input data provided"
            },
            {
                "code": 500,
                "message": "Error retrieving record"
            }
        ]
    )
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

    @swagger.operation(
        notes='Add a new listing',
        parameters=[
            {
                "name": "listing",
                "dataType": "string",
                "allowMultiple": False,
                "description": "The listing hash being added. Expected to be a `keccak256` equivalent.",
                "required": True,
                "paramType": "body"
            },
            {
                "name": "data",
                "dataType": "array",
                "allowMultiple": False,
                "description": "An array of json elements to store",
                "required": False,
                "paramType": "body"
            }
        ],
        responseMessages=[
            {
                "code": 201,
                "message": "Success"
            },
            {
                "code": 400,
                "message": "Improper payload format"
            },
            {
                "code": 500,
                "message": "Error writing to database"
            }
        ]
    )
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

    @swagger.operation(
        notes="Delete a listing from the database",
        parameters=[
            {
                "name": "listing",
                "dataType": "string",
                "allowMultiple": False,
                "description": "The listing hash being deleted",
                "required": True,
                "paramType": "body"
            }
        ],
        responseMessages=[
            {
                "code": 200,
                "message": "Item deleted"
            },
            {
                "code": 400,
                "message": "No input data provided"
            },
            {
                "code": 500,
                "message": "Error deleting record"
            }
        ]
    )
    def delete(self):
        json_data = request.get_json(force=True)
        data = json_data
        if not json_data:
            return {'message': 'No input data provided'}, 400
        response = self.db.delete_listing(json_data)
        if response == 'Error deleting record':
            return {'message': response }, 500
        else:
            return {'message': response}, 200
