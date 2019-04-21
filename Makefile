export
PYTHONPATH := .

test:
	FLASK_CONFIGURATION=test python -m pytest

run:
	FLASK_ENV=development FLASK_CONFIGURATION=dev FLASK_APP=app.py python -m flask run

docker-build:
	docker build -t datatrust:local .

docker-deploy:
	docker build -t datatrust:local .
	eval $(aws ecr get-login --no-include-email --region us-west-1 --profile computable)
	docker tag datatrust:local 365035671514.dkr.ecr.us-west-1.amazonaws.com/computable/datatrust-api:latest
    docker push 365035671514.dkr.ecr.us-west-1.amazonaws.com/computable/datatrust-api:latest
