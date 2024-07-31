.PHONY: build up down logs test

build:
	@docker-compose -f infrastructure/docker-compose.yml build

up:
	@docker-compose -f infrastructure/docker-compose.yml up -d

down:
	@docker-compose -f infrastructure/docker-compose.yml down

logs:
	@docker-compose -f infrastructure/docker-compose.yml logs -f

test:
	@docker-compose -f infrastructure/docker-compose.yml run app pytest
