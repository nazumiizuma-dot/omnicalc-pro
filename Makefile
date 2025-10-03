.PHONY: dev up build test

dev:
	docker-compose up --build

up:
	docker-compose up -d

build:
	docker-compose build

test:
	pytest -q backend/app/tests
	cd frontend && npm run test
