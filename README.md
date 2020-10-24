# 2014 i2b2 NLP Sandbox Data Node

[![GitHub CI](https://img.shields.io/github/workflow/status/Sage-Bionetworks/nlp-sandbox-data-node-i2b2-2014/ci.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/Sage-Bionetworks/nlp-sandbox-data-node-i2b2-2014)
[![GitHub Release](https://img.shields.io/github/release/Sage-Bionetworks/nlp-sandbox-data-node-i2b2-2014.svg?include_prereleases&color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/Sage-Bionetworks/nlp-sandbox-data-node-i2b2-2014/releases)
[![Docker Pulls](https://img.shields.io/docker/pulls/nlpsandbox/data-node-i2b2-2014.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/nlpsandbox/data-node-i2b2-2014)
[![GitHub License](https://img.shields.io/github/license/Sage-Bionetworks/nlp-sandbox-data-node-i2b2-2014.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/Sage-Bionetworks/nlp-sandbox-data-node-i2b2-2014)

This NLP Sandbox Data Node contains the data from the [2014 i2b2 NLP De-identification Challenge].

## Introduction



## Specifications

TBA

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

### Update the codebase when a new OpenAPI spec is available

When a new API has been released there are 2 ways to update this repository
with the new specification.

The procedure in both cases starts by checking out the [nlp-sandbox-schemas](https://github.com/Sage-Bionetworks/nlp-sandbox-schemas) repository that contains the
newest API Specification of all NLP Sandbox projects. Make sure you have the prerequisits installed for that project
before proceeding. These instructions assume you have checked out ALL projects to your home directory
identified as ~ in the following documentation. Start by running the following:

    cd ~/nlp-sandbox-schemas
    npm run build openapi/data-node/openapi.yaml

This will generate an output file dist.yaml in the current directory. It should output the following:

    npm run build openapi/data-node/openapi.yaml
    
    > nlp-sandbox-schemas@0.1.6 build ~/nlp-sandbox-schemas
    > openapi bundle -o dist $npm_config_entrypoint "openapi/data-node/openapi.yaml"
    
    bundling openapi/data-node/openapi.yaml...
    📦 Created a bundle for openapi/data-node/openapi.yaml at dist.yaml in 38ms.


Next to re-generate the flask app using one  of two methods.

The first is the easiest and least error prone if you are worried about overriding existing files.
One can generate a new flask app in a "test" directory and compare results between the old and new
directories . This is done with the command:

    openapi-generator generate -i dist.yaml -g python-flask -o ~/nlp-sandbox-data-node-i2b2-2014-updated/server

Then compare the ~/nlp-sandbox-data-node-i2b2-2014-updated/server to your existing ~/nlp-sandbox-data-node-i2b2-2014/server directory to see
what was updated.

The other method, once you are more confident, is to lay the files on top of the existing repository you've already checked with the command:

    openapi-generator generate -i dist.yaml -g python-flask -o ~/nlp-sandbox-data-node-i2b2-2014/server

If one wants to prevent certain files you know have already been customized then add those file names
cto the ~/nlp-sandbox-data-node-i2b2-2014/server/.openapi-generator-ignore file before running the preceding command.

Then use git to see what is updated and if you overwrote any files you wanted
to preserve. One can revert those changes and add those files to the .openapi-generator-ignore file for next time there is an update.

## Errors

Columns found incorrect in database :

``` psycopg2.errors.UndefinedColumn: column "filename" of relation "pat_notes" does not exist ```

There nay be times when the Database node needs to be upgraded. As the
database is stored in a volume, just remove that volume and it will
be re-created with the new files

 docker volume rm  nlp-sandbox-data-node-i2b2-2014_database-data

## Access logs

The current logs are saved to `/var/log/app/current`.

    $ docker exec data-node-api cat /var/log/app/current
    2020-09-25 23:33:39.809826500  Starting data node server
    2020-09-25 23:33:40.436453500   * Serving Flask app "__main__" (lazy loading)
    2020-09-25 23:33:40.436461500   * Environment: production
    2020-09-25 23:33:40.436462500     WARNING: This is a development server. Do not use it in a production deployment.
    2020-09-25 23:33:40.436463500     Use a production WSGI server instead.
    2020-09-25 23:33:40.436464500   * Debug mode: off

Follow the logs using `docker logs`

    docker logs --follow data-node-api

<!-- ## Deploy using Python (for development)

1. Install the dependencies

        pip install -r requirements.txt

2. Create the file that contains the future environment variables

        cp .env.sample .env

3. Set the configuration values in `.env` (see previous section)

4. Export the variables defined in *.env* to environment variables

        export $(grep -v '^#' .env | xargs -d '\n') -->

<!-- Definitions -->

[2014 i2b2 NLP De-identification Challenge]: https://www.i2b2.org/NLP/HeartDisease/