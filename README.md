# 2014-i2b2-deid-db

[![GitHub Stars](https://img.shields.io/github/stars/data2health/2014-i2b2-deid-db.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/data2health/2014-i2b2-deid-db)
[![GitHub CI](https://img.shields.io/github/workflow/status/data2health/2014-i2b2-deid-db/ci.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/data2health/2014-i2b2-deid-db)
[![GitHub License](https://img.shields.io/github/license/data2health/2014-i2b2-deid-db.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/data2health/2014-i2b2-deid-db)

This NLP Sandbox Data Node exposes the dataset of the [2014 i2b2 NLP
De-identification Challenge] through a REST API.

## Deploy using Docker

1. Create the file that contains the future environment variables

        cp .env.sample .env

2. In *.env*, set the values of `SYNAPSE_USERNAME` and `SYNAPSE_APIKEY` with the
   credentials of a Synapse account. This information is required to enable the
   Data Node to download the 2014 i2b2 data from Synapse in order to populate
   the Data Node database.

3. Export the variables defined in *.env* to environment variables

        export $(grep -v '^#' .env | xargs -d '\n')

4. Start the Data Node web service (RESP API)

        docker-compose up

5. In your browser, go to the web service documentation page
   <http://localhost:8080/api/v1/ui/> to check that the web service of the Data
   Node started successfully.

<!-- ## Deploy using Python (for development)

1. Install the dependencies

        pip install -r requirements.txt

2. Create the file that contains the future environment variables

        cp .env.sample .env

3. Set the configuration values in `.env` (see previous section)

4. Export the variables defined in *.env* to environment variables

        export $(grep -v '^#' .env | xargs -d '\n') -->
