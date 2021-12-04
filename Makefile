.DEFAULT_GOAL := help

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: build-package
build-package: ## Builds the package 
	python setup.py sdist bdist_wheel

.PHONY: clean-buid
clean-build: ## Cleans the build
	python setup.py clean --all bdist_wheel

.PHONY: validate-build
validate-build: ## Validates the build
	twine check dist/*

.PHONY: publish-pypi-test
publish-pypi-test: ## Publish on pypi test
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

.PHONY: publish-pypi-live
publish-pypi-live: ## Publish on pypi live
	twine upload dist/*

.PHONY: bumpversion-minor
bumpversion-minor: ## Bump minor version
	bumpversion --current-version $(version) minor src/__init__.py
