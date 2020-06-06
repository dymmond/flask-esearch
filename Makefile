build-package:
	python setup.py sdist bdist_wheel

clean-build:
	python setup.py clean --all bdist_wheel

validate-build:
	twine check dist/*

publish-pypi-test:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

publish-pypi-live:
	twine upload dist/*

bumpversion-minor:
	bumpversion --current-version $(version) minor src/__init__.py
