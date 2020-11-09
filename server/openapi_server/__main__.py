#!/usr/bin/env python3

import connexion
import pymongo
from mongoengine import connect, Document, StringField

from openapi_server import encoder
from openapi_server.config import Config as config


class Dataset(Document):
    name = StringField(required=True)


app = connexion.App(__name__, specification_dir='./openapi/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('openapi.yaml',
            arguments={'title': 'NLP Sandbox Data Node API'},
            pythonic_params=True)

print(f"pymongo.version: {pymongo.version}")

client = connect(
    db='nlpsandbox',
    username='nlpmongo',
    password='nlpmongo',
    host='mongodb://nlpmongo:nlpmongo@localhost/nlpsandbox'
)

print(f"server info: {client.server_info()}")

# d1 = Dataset(name='my-dataset').save()



def main():
    # TODO: Consider using param host="0.0.0.0", debug=True,
    app.run(port=config().server_port)


if __name__ == '__main__':
    main()
