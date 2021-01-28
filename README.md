# NLP Sandbox Data Node

[![GitHub Release](https://img.shields.io/github/release/nlpsandbox/data-node.svg?include_prereleases&color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/nlpsandbox/data-node/releases)
[![GitHub CI](https://img.shields.io/github/workflow/status/nlpsandbox/data-node/ci.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/nlpsandbox/data-node)
[![GitHub License](https://img.shields.io/github/license/nlpsandbox/data-node.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/nlpsandbox/data-node)
[![Docker Pulls](https://img.shields.io/docker/pulls/nlpsandbox/data-node.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/nlpsandbox/data-node)
[![Discord](https://img.shields.io/discord/770484164393828373.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=Discord&logo=discord)](https://discord.gg/Zb4ymtF "Realtime support / chat with the community and the team")
[![Coverage Status](https://img.shields.io/coveralls/github/nlpsandbox/data-node.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=coverage&logo=Coveralls)](https://coveralls.io/github/nlpsandbox/data-node?branch=)

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

2. Start the Data Node API service

       docker-compose up

3. In your browser, go to the web service documentation page
   <http://localhost:8080/api/v1/ui/> to check that the web service of the Data
   Node started successfully.

<!-- Definitions -->

[NLP Sandbox Date Node OpenAPI specification]: https://github.com/Sage-Bionetworks/nlp-sandbox-schemas