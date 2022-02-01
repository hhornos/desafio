MSG = $1

-include .env
export


requirements-dev-install:
	pip install -r requirements-dev.txt

requirements-install:
	pip install -r requirements.txt

run:
	python main.py

test:
	pytest tests/unit

integration-test:
	pytest tests/integration

coverage:
	pytest tests --doctest-modules --junitxml=junit/test-results.xml --cov=app --cov-report=xml --cov-report=html

lint:
	pylint app

generate-docs:
	python generate_docs.py

deploy:
	gcloud app deploy app.yaml

router-config:
	gcloud app deploy dispatch.yaml

create-database:
	alembic revision -m "create first database revision"

create-migrations:
	alembic revision --autogenerate -m "${MSG}"

migrate:
	alembic upgrade head
