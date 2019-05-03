"""
Flask entry point
"""

import os
from flask import Flask, Blueprint
from flask_restful import Api
from flask_restful_swagger import swagger
import config
from db.connectionManager import ConnectionManager
from api.v1.listing import Listing

CONFIGS = {
    'production': config.ProdConfig,
    'dev': config.DevConfig,
    'test': config.TestConfig,
    'default': config.DevConfig
}
config_name = os.getenv('FLASK_CONFIGURATION', 'default')

# Setup Flask Environment
app = Flask(__name__)
app.config.from_object(CONFIGS[config_name])
api_blueprint = Blueprint('api', __name__)
api = swagger.docs(
    Api(api_blueprint),
    apiVersion='0.1',
    description='Swagger (Open API Spec) documentation for Datatrust'
)
print(app.config['STARTUP_MSG'])

# Initialize DB Connection
db = ConnectionManager(app.config['DB_URL'], app.config['LOCAL'], app.config['TABLE_NAME'], app.config['REGION'])

# Endpoints
api.add_resource(Listing, '/api/v1/listing', resource_class_kwargs={'db': db})
app.register_blueprint(api_blueprint)

# Health check
@app.route('/health', methods=['GET'])
def health():
    return 'OK'
