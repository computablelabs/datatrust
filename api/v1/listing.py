"""
Resource definition for Drive Listing
"""

from datetime import datetime
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
            obfuscated_response = self.obfuscate_listing(response)
            return obfuscated_response, 200

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

    def elapsed_time(self, start, end):
        """
        Return a reasonable number for elapsed time
        :param start: datetime
        :param end: datetime
        :return: elapsed: string
        """
        duration = end - start
        if duration.days == 0:
            if duration.seconds > 3600:
                return f'~{duration.seconds // 3600} hours'
            elif duration.seconds > 60:
                return f'~{duration.seconds // 60} minutes'
            else:
                return f'~{duration.seconds} seconds'
        else:
            return f'{duration.days} days'

    def obfuscate_listing(self, listing):
        """
        Obfuscate the data returned from the db before presenting to the client
        Fields returned:
        listing: string: hash of the listing (a.k.a. id)
        num_data_points: int: number of data points in the listing
        avg_velocity: float: average velocity across all data points
        duration: string: elapsed time between first and last data point
        start_location: string: City, State location of the first data point
        end_location: string: City, State location of the last data point
        :param listing: dict: a Drive listing
        :return: obfuscated: dict: an obfuscated listing
        """
        obfuscated = {}
        obfuscated['listing'] = listing['listing']
        obfuscated['num_data_points'] = len(listing['data'])
        sum_velocity = 0
        velocity_points = 0
        start_timestamp = datetime.now()
        end_timestamp = datetime(1970, 1, 1, 12, 0, 0)
        start_location = None
        end_location = None
        for location in listing['data']:
            if 'velocity' in location:
                sum_velocity += float(location['velocity'])
                velocity_points += 1
            if 'adjusted_timestamp' in location:
                ts = datetime.strptime(location['adjusted_timestamp'], '%Y-%m-%d %H:%M:%S.%f')
                if ts < start_timestamp:
                    start_timestamp = ts
                    if 'latitude' and 'longitude' in location:
                        lat = round(float(location['latitude']), 2)
                        long = round(float(location['longitude']), 2)
                        start_location = f"{lat}, {long}"
                if ts > end_timestamp:
                    end_timestamp = ts
                    if 'latitude' and 'longitude' in location:
                        lat = round(float(location['latitude']), 2)
                        long = round(float(location['longitude']), 2)
                        end_location = f"{lat}, {long}"
        obfuscated['avg_velocity'] = sum_velocity / velocity_points
        obfuscated['duration'] = self.elapsed_time(start_timestamp, end_timestamp)
        obfuscated['start_location'] = start_location
        obfuscated['end_location'] = end_location
        return obfuscated
