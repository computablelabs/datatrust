"""
Flask entry point
"""

import os
from flask import Flask, Blueprint
from flask_restful import Api, Resource
import config
from api.v1.listing import Listing

CONFIGS = {
    'production': config.ProdConfig,
    'default': config.DevConfig
}
config_name = os.getenv('FLASK_CONFIGURATION', 'default')

app = Flask(__name__)
app.config.from_object(CONFIGS[config_name])
api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)
print(app.config['STARTUP_MSG'])

api.add_resource(Listing, '/api/v1/listing')
app.register_blueprint(api_blueprint)

@app.route('/health', methods=['GET'])
def health():
    return 'OK'
