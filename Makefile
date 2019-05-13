export
PYTHONPATH := .

test:
	FLASK_CONFIGURATION=test python -m pytest

run:
	# Start dev dynamodb with java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb
	FLASK_ENV=development FLASK_CONFIGURATION=dev FLASK_APP=app.py python -m flask run

run-prod:
	FLASK_ENV=production FLASK_CONFIGURATION=production FLASK_APP=app.py python -m flask run

docker-build:
	docker build -t datatrust:local .

docker-deploy:
	docker build -t datatrust:local .
	$(shell aws ecr get-login --no-include-email --region us-west-1 --profile computable)
	docker tag datatrust:local 365035671514.dkr.ecr.us-west-1.amazonaws.com/computable/datatrust-api:latest
	docker push 365035671514.dkr.ecr.us-west-1.amazonaws.com/computable/datatrust-api:latest
