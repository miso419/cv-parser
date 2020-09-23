.PHONY: help prepare-dev test lint run doc

NAME=ai-service
VENV_NAME?=venv
PYTHON=${VENV_NAME}/bin/python3
PIP=${VENV_NAME}/bin/pip3

.DEFAULT: help
help:
	@echo "make prepare-dev"
	@echo "       prepare development environment, use only once"
	@echo "make test"
	@echo "       run tests"
	@echo "make lint"
	@echo "       run pylint"
	@echo "make run"
	@echo "       run project"
	@echo "make docker-build"
	@echo "       build a docker image"
	@echo "make docker-run"
	@echo "       run a docker container with the image"

prepare-dev:
	python3 -m pip install virtualenv
	make venv

venv: requirements.txt
	test -d $(VENV_NAME) || virtualenv $(VENV_NAME)
	. $(VENV_NAME)/bin/activate; pip3 install -Ur requirements.txt
	touch $(VENV_NAME)/bin/activate
	${PYTHON} -m spacy download en_core_web_lg

test: venv
	${PYTHON} -m pytest -s

lint: venv
	pylint app
	pylint run.py

run: venv
	${PYTHON} run.py

get-packages: venv
	${PIP} freeze

docker-build:
	docker build -t ai-service-image .

docker-run:
	docker run -p 8085:4005 --name ai-service -d ai-service-image
