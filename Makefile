.PHONY: install
install:
	poetry lock --no-update
	poetry install

.PHONY: test
test:
	poetry run pytest --color=yes --cov-report xml --cov=tp1_gl5_devops
	poetry run coverage report --skip-covered --skip-empty
	poetry run coverage xml