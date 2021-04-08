.PHONY: help

help: 
	@echo "Show  Help text "
 
menu:
	@echo "Show de Options "

build-rm: 
	@echo "Clean package"
	rm -rf dist
	rm -rf devops.egg-info

build: build-rm 
	@echo "Creating build package"
	python setup.py sdist

deploy-pip-dev: build
	@echo " Send the code to PIP server DEV "
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

deploy-pip-prod: build
	@echo "Sending the code to PIP server PROD"
	#twine upload dist/*

clean-virtual:
	@echo "Clena a virtual ambient"
	deactivate
	rm -rf virtual

create-virtual: clean-virtual
	@echo " Creating a virtual ambient"
	python3 -m venv virtual
	pip install --upgrade pip
	pip install setuptools wheel twine