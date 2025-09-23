.PHONY: test build

test:
	python -m unittest discover -s test

build:
	docker build -t product-inventory .


