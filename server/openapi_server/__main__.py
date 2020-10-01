#!/usr/bin/env python3

import connexion
from openapi_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': '2014 i2b2 NLP Sandbox Data Node'},
                pythonic_params=True)

    # TODO: Read port from env vars
    app.run(port=8080, ssl_context=('server.crt', 'server.key'))


if __name__ == '__main__':
    main()
