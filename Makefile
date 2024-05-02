VERSION ?= 0.1.3
CACHE ?= --no-cache=1

.PHONY: default all build-docker publish-docker install clean
default: checktest
all: build-docker publish-docker
build-docker:
	docker buildx build --platform linux/arm/v7,linux/arm64/v8,linux/amd64,linux/arm/v6,linux/s390x,linux/386 ${PUSH} --build-arg VERSION=${VERSION} --tag jaymoulin/google-chrome-webstore-download --tag jaymoulin/google-chrome-webstore-download:${VERSION} ${CACHE} -f docker/Dockerfile .
publish-docker:
	PUSH=--push CACHE= make build
checktest: install
	twine upload -r testpypi dist/*
publish: install
	twine upload dist/*
install: clean check
	sudo python3 setup.py sdist
check:
	python3 setup.py check --restructuredtext
build:
	mkdir -p build
dist:
	mkdir -p dist
clean: build dist
	sudo rm -Rf build/*
	sudo rm -Rf dist/*
