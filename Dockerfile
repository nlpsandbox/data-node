FROM python:3.7.9-slim-buster
RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/src/init

COPY flask-app/ /usr/src/app
COPY init /usr/src/init

WORKDIR /usr/src/app
RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "openapi_server"]
