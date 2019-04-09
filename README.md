[![Build Status](https://travis-ci.org/computablelabs/datatrust.svg?branch=master)](https://travis-ci.org/computablelabs/datatrust)

# datatrust
A Computable Datatrust implementation written in Python 

## Setup

Tested with Python 3.7. Other 3.x versions may work as well. Python2 will not work.

- Create a python3.7 virtual environment `{PATH_TO_PYTHON_3.7} -m venv .env`

- Activate the virtual environment `source .env/bin/activate`

- Install dependencies `pip install -r requirements.txt`

## Running Locally

- For development work:
- `make dev`

_*Dev requires a local dynamodb database. Download it [here](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html)*_


- For production:
- `FLASK_CONFIGURATION=production FLASK_APP=app.py python -m flask run`

## Usage

Post data to the API endpoint `api/v1/listing` 

Curl example:

```
curl -X POST \
  http://localhost:5000/api/v1/listing \
  -H 'Content-Type: application/json' \
  -d '{
	"listing": "willtest1",
	"data": [
		{"foo": "bar"},
		{"baz": "bang"}
	]
}'
```

`listing` is required in the json payload, `data` is currently not

## Testing

- `make test`

- _NOTE: Two warnings appear in test results due to unresolved deprecation warnings in Jinja2_
