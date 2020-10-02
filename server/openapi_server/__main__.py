#!/usr/bin/env python3

import connexion
from openapi_server import encoder
from openapi_server.util.configuration import CD2HConfig as config


def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': '2014 i2b2 NLP Sandbox Data Node'},
                pythonic_params=True)

    flask_port = config().flask_port
    print(f"Starting on port  {flask_port}")
    app.run(port=flask_port)


if __name__ == '__main__':
    main()
