FROM python:alpine

MAINTAINER Jay MOULIN <jaymoulin@gmail.com>

RUN apk update && \
    apk add g++ --virtual .build-deps && \
    pip3 install chrome-webstore-download && \
    apk del g++ --purge .build-deps

ADD ./entrypoint.sh /usr/bin/entrypoint

VOLUME /root

WORKDIR /root
ENTRYPOINT ["entrypoint"]
