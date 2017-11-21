VERSION ?= 0.1.0
FULLVERSION ?= ${VERSION}
archs = s390x arm32v7 amd64 ppc64le i386 arm64v8 arm32v6 arm32v5

.PHONY: all build publish latest
all: build publish
build:
	cp /usr/bin/qemu-*-static .
	$(foreach arch,$(archs), \
		cat docker/Dockerfile | sed "s/FROM python:alpine/FROM ${arch}\/python:alpine/g" > .Dockerfile; \
		docker build -t jaymoulin/google-chrome-webstore-download:${VERSION}-$(arch) -f .Dockerfile .;\
	)
publish:
	docker push jaymoulin/google-chrome-webstore-download
	cat manifest.yml | sed "s/\$$VERSION/${VERSION}/g" > manifest.yaml
	cat manifest.yaml | sed "s/\$$FULLVERSION/${FULLVERSION}/g" > manifest2.yaml
	mv manifest2.yaml manifest.yaml
	manifest-tool push from-spec manifest.yaml
latest: build
	FULLVERSION=latest VERSION=${VERSION} make publish
