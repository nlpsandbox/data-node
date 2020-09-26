#!/usr/bin/env python3

import click
import os
import synapseclient
import zipfile, tarfile
import db_connection as db
import logging

@click.group()
def cli():
    """Initialize a DB with the 2014 i2b2 NLP de-id data."""

@cli.command()
def populate_db():
    """Populate the DB with 2014 i2b2 NLP de-id data."""
    values = db.load_config()
    # logging.info(values)
    # logging.info("Started import ")
    # logging.info(f'Importing into DB: {values["database"]}')
    # host, db, user, password
    conn = db.get_connection_local_pg( values)
    # logging.info("Finished import ")
    if ( not os.path.isdir("/tmp/data/2014-i2b2-nlp-evaluation-data-txt") ):
        logging.exception("Data not downloaded, run the main.py get_data first  ")
        os.sys.exit(1)
    db.import_data(conn, "/tmp/data/2014-i2b2-nlp-evaluation-data-txt", "/tmp/data/testing-PHI-Gold-fixed")

if __name__ == "__main__":
    cli()
