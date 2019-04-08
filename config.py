import os

class BaseConfig(object):
    """
    Config vars for app
    """
    DEBUG = False
    TESTING = False
    STARTUP_MSG = 'Using BaseConfig'

class DevConfig(BaseConfig):
    """
    Configuration for dev work
    """
    DEBUG = True
    STARTUP_MSG = 'Using DevConfig'
    LOCAL = True
    DB_URL = 'http://localhost:8000'
    TABLE_NAME = 'drive_dev'
    AWS_ACCESS_KEY_ID='fake'
    AWS_SECRET_ACCESS_KEY='faketoo'

class TestConfig(BaseConfig):
    """
    Configuration for running tests
    """
    TESTING = True
    LOCAL = False
    DB_URL = None
    TABLE_NAME = 'drive_test'

class ProdConfig(BaseConfig):
    """
    Configuration for production
    """
    DB = os.getenv('DB')
    STARTUP_MSG = 'Using ProdConfig'