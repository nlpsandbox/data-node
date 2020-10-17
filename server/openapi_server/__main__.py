#!/usr/bin/env python3

import connexion
from openapi_server import encoder
from logging.config import dictConfig
from openapi_server.util.configuration import Config as config


def main():
    # Set up logging
    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    })

    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.logger.warning("Startup of Server...")
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': '2014 i2b2 NLP Sandbox Data Node'},
                pythonic_params=True)

    server_port = config().server_port
    print(f"Starting on port  {server_port}")
    app.run(port=server_port)
    app.app.logger.warning("Stopping of Server...")


if __name__ == '__main__':
    main()
