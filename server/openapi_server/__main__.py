#!/usr/bin/env python3

import connexion
from mongoengine import connect

from openapi_server import encoder
from openapi_server.config import Config as config


app = connexion.App(__name__, specification_dir='./openapi/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('openapi.yaml', pythonic_params=True)

connect(
    db=config().db_database,
    username=config().db_username,
    password=config().db_password,
    host=config().db_host
)


def main():
    app.run(port=config().server_port, debug=False)


if __name__ == '__main__':
    main()
