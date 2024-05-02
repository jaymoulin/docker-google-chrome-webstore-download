FROM python:alpine

ARG VERSION
ARG TARGETPLATFORM
LABEL MAINTAINER="Jay MOULIN <https://jaymoulin.me>"
LABEL version="${VERSION}-${TARGETPLATFORM}"

RUN apk update && \
    apk add g++ --virtual .build-deps && \
    pip3 install chrome-webstore-download && \
    apk del g++ --purge .build-deps

ADD ../entrypoint.sh /usr/bin/entrypoint

VOLUME /root

WORKDIR /root
ENTRYPOINT ["entrypoint"]
