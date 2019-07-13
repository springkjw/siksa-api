build: ## 도커 이미지 빌드
	docker-compose build

dev: build
	docker-compose -f docker-compose.dev.yml up -d

stop:
	docker-compose down --volumes --remove-orphans

shell:
	docker-compose exec app bash

# .DEFAULT_GOAL:=help

# ##@ 설치하기
# .PHONY: build

# .PHONY: install

# install: build ## 프로젝트 설치 및 Composer 패키지 설치
# 	docker-compose run --rm install

# composer: build ## Composer 실행
# 	docker-compose up -d install
# 	docker-compose exec install bash

# ##@ 구동하기
# dev: stop build ## 로컬 서버 구동
# 	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d nginx postgres adminer php
# 	docker-compose exec -u 1000:1000 php sh -c "php artisan migrate && php artisan db:seed"

# stop: ## 서버 중단
# 	docker-compose down --volumes --remove-orphans

# shell: ## php 쉘 bash 접속
# 	docker-compose exec -u 1000:1000 php bash

# update: stop ## 서버 중단 및 코드 업데이트
# 	git pull origin master
 
# deploy: stop build ## 배포하기
# 	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d nginx php adminer
# 	docker-compose exec -u 1000:1000 php sh -c "php artisan migrate --env=production"

# .PHONY: help
# help:
# 	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)