FROM python:3.7.9-slim-buster
RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/src/init

COPY flask-app/ /usr/src/app
COPY init /usr/src/init
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN apt-get update; apt-get install -y supervisor
RUN pip3 install --no-cache-dir supervisor
RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt

WORKDIR /usr/src/app
EXPOSE 8080

CMD ["/usr/bin/supervisord"]
