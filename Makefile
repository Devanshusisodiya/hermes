.PHONY: lint
lint:
	tox -e pylint
	tox -e flake8

.PHONY: type-check
type-check:
	tox -e mypy

.PHONY: format
format:
	tox -e isort
	tox -e black