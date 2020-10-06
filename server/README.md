# 2014 i2b2 NLP Sandbox Data Node
## Developer Notes

The following environment variables can be set in the shell before starting
the flask app to override the default values:

    export SQL_USER=postgres
    export SQL_PASSWORD=postgres
    export SQL_DB=i2b2_data
    export SQL_PORT=5432
    export SQL_HOST=database
    export SQL_DB_TYPE=postgres


    export SYNAPSE_USERNAME=george.kowalski@gmail.com
    export SYNAPSE_APIKEY=aieCjlhkQViK/uyNVimJAyoJxYOIo9iCLlCE/BAWWhNmrLtcgXoKrwuWrRpVCSxh/ySDy/lucTXaJFyyfqFa5w==


This NLP Sandbox Data Node exposes the dataset of the [2014 i2b2 NLP
De-identification Challenge] through a REST API.

## Overview

TODO

## Run with Docker

Build a Docker image that includes this server

    docker build -t openapi_server .

Run the dockerized server

    docker run -p 8080:8080 openapi_server

Open your browser and navigate to <http://localhost:8080/api/v1/ui/> to check that
the server is running. This page lists the specifications of the API requests
that can be sent to this service.

The OpenAPI specifications implemented by this server live here:

<http://localhost:8080/api/v1/openapi.json>

## Run manually

Check that your Python version is 3.7+

    $ python --version
    Python 3.7.9

Install the server dependencies

    pip install -r requirements.txt

Start the server

    python -m openapi_server

## Set up SSL For Flask
This is done to generate a Self Signed Server Key and Certificate used in
starting the Flask app using SSL. It will still use the port set as SERVER_PORT.

The cert generated will only work for https://localhost

    openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -out server.pass.key
    openssl rsa -passin pass:x -in server.pass.key -out server.key
    openssl req -new -key server.key -out server.csr -subj "/C=US/ST=Wisconsin/L=Milwaukee/O=OrgName/OU=CTSI/CN=localhost"
    openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt

The resulting cert.key and server.crt can be copied into the server directory where it will be used
on startup \_\_main\_\_.py


## Run the integration tests

To launch the integration tests, use tox

    pip install tox
    tox

## Update the server OpenAPI specifications

TODO

<!-- Definitions -->

[2014 i2b2 NLP De-identification Challenge]: https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/
[OpenAPI Generator]: https://openapi-generator.tech