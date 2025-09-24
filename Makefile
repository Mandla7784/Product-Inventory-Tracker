.PHONY: test build

test:
	python -m unittest discover -s inventory/tests -p "test_*.py"

build:
	docker build -t mandla8080/product-inventory:latest .

push:
	docker push mandla8080/product-inventory:latest
