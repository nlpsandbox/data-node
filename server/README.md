# 2014 i2b2 NLP Sandbox Data Node


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

## Run the integration tests

To launch the integration tests, use tox

    pip install tox
    tox

## Update the server OpenAPI specifications

TODO

<!-- Definitions -->

[2014 i2b2 NLP De-identification Challenge]: https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/
[OpenAPI Generator]: https://openapi-generator.tech