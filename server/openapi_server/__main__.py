#!/usr/bin/env python3

import connexion

from openapi_server import encoder
from openapi_server.config import Config as config

app = connexion.App(__name__, specification_dir='./openapi/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('openapi.yaml',
            arguments={'title': 'NLP Sandbox Data Node API'},
            pythonic_params=True)


def main():
    # TODO: Consider using param host="0.0.0.0", debug=True,
    app.run(port=config().server_port)


if __name__ == '__main__':
    main()
