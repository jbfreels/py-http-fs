.PHONY: help

help: ## help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

build: 	## build image
	docker build --no-cache -t py-http .

run: ## start container with no authentication
	docker rm -f py-http
	docker run -d \
		-p 8081:80 \
		--name py-http \
		-v /tmp:/data \
		py-http

run-with-auth: ## start container with basic authentication
	docker rm -f py-http
	docker run -d \
		-p 8081:80 \
		--name py-http \
		-v /tmp:/data \
		-e USERNAME='share' \
		-e PASSWORD='password' \
		py-http