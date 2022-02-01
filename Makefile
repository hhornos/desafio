MSG = $1

-include .env
export

requirements-update:
	python -m piptools compile --allow-unsafe --generate-hashes requirements.in --output-file requirements.txt
	python -m piptools compile --allow-unsafe --generate-hashes requirements-dev.in --output-file requirements-dev.txt

requirements-dev-install:
	python -m piptools sync requirements-dev.txt requirements.txt

requirements-install:
	python -m piptools sync requirements.txt

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

create_migrations:
	alembic revision --autogenerate -m "${MSG}"

migrate:
	alembic upgrade head
