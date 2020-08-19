#!/usr/bin/env python3

import click
import os
import synapseclient
import zipfile

@click.group()
def cli():
    """Initialize a DB with the 2014 i2b2 NLP de-id data."""

@cli.command()
@click.option('--synapse-username', help='Synapse username',
              type=str, default=lambda: os.environ.get('SYNAPSE_USERNAME', ''))
@click.option('--synapse-apikey', help='Synapse API Key',
              type=str, default=lambda: os.environ.get('SYNAPSE_APIKEY', ''))
def get_data(synapse_username, synapse_apikey):
    """Get 2014 i2b2 NLP de-id data from Synapse."""
    syn = synapseclient.Synapse()
    syn.login(email=synapse_username, apiKey=synapse_apikey, silent=True)

    # Download the evaluation and training set
    eval_data_entity = syn.get('syn22314948')
    train_data_entity = syn.get('syn22314947')

    # Extract the data to ./data
    with zipfile.ZipFile(eval_data_entity.path,"r") as zip:
        zip.extractall("data")
    with zipfile.ZipFile(train_data_entity.path,"r") as zip:
        zip.extractall("data")


@cli.command()
def populate_db():
    """Populate the DB with 2014 i2b2 NLP de-id data."""
    raise NotImplementedError


if __name__ == "__main__":
    cli()
