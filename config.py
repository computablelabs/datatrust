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

class ProdConfig(BaseConfig):
    """
    Configuration for production
    """
    DB = os.getenv('DB')
    STARTUP_MSG = 'Using ProdConfig'
