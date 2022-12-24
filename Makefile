VERSION ?= 0.1.3
CACHE ?= --no-cache=1
FULLVERSION ?= ${VERSION}
archs ?= s390x amd64 i386 arm64v8 arm32v6

.PHONY: default all build-docker publish-docker latest install clean
default: checktest
all: publish build-docker publish-docker latest
build-docker:
	cp /usr/bin/qemu-*-static .
	$(foreach arch,$(archs), \
		cat docker/Dockerfile | sed "s/FROM python:alpine/FROM ${arch}\/python:alpine/g" > .Dockerfile; \
		docker build -t jaymoulin/google-chrome-webstore-download:${VERSION}-$(arch) -t ghcr.io/jaymoulin/google-chrome-webstore-download:${VERSION}-$(arch) -f .Dockerfile ${CACHE} .;\
	)
publish-docker:
	docker push jaymoulin/google-chrome-webstore-download -a
	docker push ghcr.io/jaymoulin/google-chrome-webstore-download -a
	cat manifest.yml | sed "s/\$$VERSION/${VERSION}/g" > manifest.yaml
	cat manifest.yaml | sed "s/\$$FULLVERSION/${FULLVERSION}/g" > manifest2.yaml
	mv manifest2.yaml manifest.yaml
	manifest-tool push from-spec manifest.yaml
	cat manifest.yaml | sed "s/jaymoulin/ghcr.io\/jaymoulin/g" > manifest2.yaml
	mv manifest2.yaml manifest.yaml
	manifest-tool push from-spec manifest.yaml
latest:
	FULLVERSION=latest VERSION=${VERSION} make publish-docker 
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
