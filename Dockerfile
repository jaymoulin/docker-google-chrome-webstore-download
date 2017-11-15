FROM jaymoulin/rpi-python:alpine

MAINTAINER Jay MOULIN <jaymoulin@gmail.com>

RUN pip3 install chrome-webstore-download

ADD ./entrypoint.sh /usr/bin/entrypoint

VOLUME /root

WORKDIR /root
ENTRYPOINT ["entrypoint"]
