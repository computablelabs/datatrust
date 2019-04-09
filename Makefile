export
PYTHONPATH := .

test:
	FLASK_CONFIGURATION=test python -m pytest

run:
	FLASK_ENV=development FLASK_CONFIGURATION=dev FLASK_APP=app.py python -m flask run

docker:
	docker build -t datatrust:local .
