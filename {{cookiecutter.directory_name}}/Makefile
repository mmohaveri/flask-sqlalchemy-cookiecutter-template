PROJECT_NAME := {{cookiecutter.directory_name}}
PROJECT_PATH := {{cookiecutter.project_git_path}}/$(PROJECT_NAME)

COMMIT := $(shell git rev-parse HEAD 2> /dev/null || echo "NULL")
VERSION := $(shell git describe $(COMMIT) 2> /dev/null || echo "$(COMMIT)")
IMAGE_NAME := {{cookiecutter.docker_registry_path}}/$(PROJECT_PATH)
IMAGE_VERSION := $(VERSION)

PROJECT_FILES := $(shell find $(PROJECT_NAME) -name "*.py" 2> /dev/null || echo "NULL")
TEST_FILES := $(shell find tests -name "test_*.py" 2> /dev/null || echo "NULL")

help: ## Display this help screen
	@grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

clean: ## Remove auto generated files
	@find {{cookiecutter.project_name}} -type f -name "*.py[oc]" -delete
	@find {{cookiecutter.project_name}} -type d -name __pycache__ -delete

requirements: requirements.txt ##install project requirements
	pip install -r requirements.txt

development-requirements: requirements.development.txt ##install project's development requirements
	pip install -r requirements.development.txt

.SECONDEXPANSION:
test: requirements $(PROJECT_FILES) $(TEST_FILES) ## run tests
	python -m unittest discover tests

.SECONDEXPANSION:
coverage: requirements $(PROJECT_FILES) $(TEST_FILES) ## get coverage report
	py.test --cov={{cookiecutter.project_name}} tests

.SECONDEXPANSION:
docker: $(PROJECT_FILES) ## build docker image
	@docker build -t $(IMAGE_NAME):$(IMAGE_VERSION) .

push: docker ## push docker image to registry
	@docker push $(IMAGE_NAME):$(VERSION)

.PHONY: help clean requirements development-requirements test coverage coverage docker push