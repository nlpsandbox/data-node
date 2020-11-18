# NLP Sandbox Data Node

[![Docker Pulls](https://img.shields.io/docker/pulls/nlpsandbox/data-node.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/nlpsandbox/data-node)
[![GitHub Release](https://img.shields.io/github/release/Sage-Bionetworks/nlp-sandbox-data-node-i2b2-2014.svg?include_prereleases&color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/Sage-Bionetworks/nlp-sandbox-data-node-i2b2-2014/releases)
[![GitHub CI](https://img.shields.io/github/workflow/status/Sage-Bionetworks/nlp-sandbox-data-node-i2b2-2014/ci.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/Sage-Bionetworks/nlp-sandbox-data-node-i2b2-2014)
[![GitHub License](https://img.shields.io/github/license/Sage-Bionetworks/nlp-sandbox-data-node-i2b2-2014.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/Sage-Bionetworks/nlp-sandbox-data-node-i2b2-2014)

Dockerized API service to store and retrieve data needed to benchmark NLP tools

## Specification

- Implements the [NLP Sandbox Date Node OpenAPI specification]
- Create and manage datasets
- Create and manage FHIR stores
  - Store and retrieve FHIR patient profiles
  - Store and retrieve clinical notes
- Create and manage annotation stores
  - Store and retrieve text annotations

## Deploy using Docker

1. Create the file that contains the future environment variables

       cp .env.sample .env

2. Export the variables defined in *.env* to environment variables

       export $(grep -v '^#' .env | xargs -d '\n')

3. Start the Data Node API service

       docker-compose up

4. In your browser, go to the web service documentation page
   <http://localhost:8080/api/v1/ui/> to check that the web service of the Data
   Node started successfully.

<!-- Definitions -->

[NLP Sandbox Date Node OpenAPI specification]: https://github.com/Sage-Bionetworks/nlp-sandbox-schemas