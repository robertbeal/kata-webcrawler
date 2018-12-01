.PHONY: build test run

default: build test

build:
	docker build -t web-crawler .

test:
	docker run --rm web-crawler nosetests tests

run:
	docker run --rm web-crawler python3 crawler/crawler.py
