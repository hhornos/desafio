-include .env
export

dev-setup:
	@poetry install

dev-services-up:
	@docker-compose up -d

create-migrations:
	@poetry run alembic revision --autogenerate -m "${msg}"

migrate:
	@poetry run alembic upgrade head

setup:
	@poetry install --no-dev

run:
	@poetry run python main.py

test:
	@poetry run pytest tests/unit

coverage:
	@poetry run pytest tests --doctest-modules --junitxml=junit/test-results.xml --cov=app --cov-report=xml --cov-report=html

lint:
	@poetry run pylint app

docs-generate:
	@poetry run python generate_docs.py

