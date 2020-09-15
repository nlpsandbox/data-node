#!/usr/bin/env python3

import connexion
from flask import render_template
from openapi_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'NLP Sandbox Data Node Schemas'},
                pythonic_params=True)

    @app.route('/')
    def home():
        """
        This function just responds to the browser ULR
        localhost:5000/
        :return:        the rendered template 'home.html'
        """
        return render_template('home.html')

    app.run(port=8080)


if __name__ == '__main__':
    main()
