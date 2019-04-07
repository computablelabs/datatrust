[![Build Status](https://travis-ci.org/computablelabs/datatrust.svg?branch=master)](https://travis-ci.org/computablelabs/datatrust)

# datatrust
A Computable Datatrust implementation written in Python 

## Setup

Tested with Python 3.7. Other 3.x versions may work as well

- Create a python3.7 virtual environment `{PATH_TO_PYTHON_3.7} -m venv .env`

- Activate the virtual environment `source .env/bin/activate`

- Install dependencies `pip install -r requirements.txt`

## Running Locally

- For development work:
- `FLASK_ENV=development FLASK_APP=app.py python -m flask run`
- For production:
- `FLASK_CONFIGURATION=production FLASK_APP=app.py python -m flask run`

## Testing

- `python -m pytest`

- _NOTE: Two warnings appear in test results due to unresolved deprecation warnings in Jinja2_
