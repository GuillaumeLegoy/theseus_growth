.PHONY: lint test

lint:
	poetry run flake8

test:
	poetry run pytest
