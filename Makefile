.PHONY: test build

test:
	python -m unittest discover -s inventory/tests -p "test_*.py"

build:
	docker build -t product-inventory .
