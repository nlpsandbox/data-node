# 2014-i2b2-deid-db

[![GitHub Stars](https://img.shields.io/github/stars/data2health/2014-i2b2-deid-db.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/data2health/2014-i2b2-deid-db)
[![GitHub CI](https://img.shields.io/github/workflow/status/data2health/2014-i2b2-deid-db/ci.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/data2health/2014-i2b2-deid-db)
[![GitHub License](https://img.shields.io/github/license/data2health/2014-i2b2-deid-db.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/data2health/2014-i2b2-deid-db)

Dockerized Postgres DB populated with data from the 2014 i2b2 NLP
de-identification challenge.

## Setup

1. Install the dependencies

        pip install -r requirements.txt

2. Copy the file `.env.template` to `.env`
3. Set the configuration values in `.env`
4. Export the configuration to environment variables

        export $(grep -v '^#' .env | xargs -d '\n')

## Usage

    $ python main.py
    Usage: main.py [OPTIONS] COMMAND [ARGS]...

    Initialize a DB with the 2014 i2b2 NLP de-id data.

    Options:
    --help  Show this message and exit.

    Commands:
    get-data     Get 2014 i2b2 NLP de-id data from Synapse.
    populate-db  Populate the DB with 2014 i2b2 NLP de-id data.


### Command `get-data`

    $ python main.py get-data
    Downloading  [####################]100.00%   1.1MB/1.1MB (2.6MB/s) 2014-i2b2-nlp-evaluation-data-txt.zip Done...
    Downloading  [####################]100.00%   1.7MB/1.7MB (11.7MB/s) 2014-i2b2-nlp-training-data-txt.zip Done...

### Command `populate-db`

Start the docker Image with first :
    docker-compose up

Then run :

    python main.py populate-db

 One should see :

    2020-08-24 15:22:20,800 root - INFO - {'host': 'localhost', 'user': 'postgres', 'password': 'postgres', 'database': 'i2b2_data', 'port': '6000'}
    2020-08-24 15:22:20,800 root - INFO - Started import 
    2020-08-24 15:22:20,800 root - INFO - Importing into DB: i2b2_data
    2020-08-24 15:22:20,809 root - INFO - PostgreSQL database version:
    2020-08-24 15:22:20,811 root - INFO - ('PostgreSQL 12.4 (Debian 12.4-1.pgdg100+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 8.3.0-6) 8.3.0, 64-bit',)
    2020-08-24 15:22:20,811 root - INFO - Finished import 
    2020-08-24 15:22:20,817 root - INFO - Importing file 137-03.txt
    2020-08-24 15:22:20,820 root - INFO - Inserted row 1 
    ...


### Flask REST Front End

Create the flask app from the https://github.com/data2health/nlp-sandbox-schemas CodeBase

    cd ~project/nlp-sandbox-schemas
    openapi/data-node/generate-flask.sh 


