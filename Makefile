.PHONY: lint
lint:
	tox -e pylint
	tox -e clean-imports
	tox -e flake8
	tox -e mypy