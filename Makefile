all: black

black:
	black --line-length 90 teampulls/

black-check:
	black --check --line-length 90 teampulls/

build: black-check
	python3 setup.py sdist bdist_wheel

test-publish: clean black-check build
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

publish: clean black-check build
	twine upload dist/*

clean:
	rm -rf build dist *.egg-info

.PHONY: black black-check build publish test-publish clean
