FROM python:3.7.9-slim-buster
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements_3_7.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r /usr/src/app/requirements_3_7.txt

COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "openapi_server"]
