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