FROM python:3.7.9-slim-buster

RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/src/init

COPY server /usr/src/app
COPY init /usr/src/init
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# hadolint ignore=DL3008
RUN apt-get update -qq -y \
    && apt-get install --no-install-recommends -qq -y \
        supervisor \
    && apt-get -y autoclean \
    && apt-get -y autoremove \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir supervisor==4.2.1
RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt

WORKDIR /usr/src/app
EXPOSE 8080

CMD ["/usr/bin/supervisord"]