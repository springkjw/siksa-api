build: ## 도커 이미지 빌드
	docker-compose build

dev: build
	docker-compose -f docker-compose.dev.yml up -d

deploy: build
	docker-compose -f docker-compose.prod.yml up -d

stop:
	docker-compose down --volumes --remove-orphans

shell:
	docker-compose exec app bash