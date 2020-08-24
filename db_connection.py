import psycopg2
import psycopg2.extras
import logging
from pathlib import Path
from configparser import ConfigParser
import logging
import os.path



def load_config(config_file="database.ini"):
    """
    Load the configuration file
    :param config_file:
    :return:
    """
    db = {}
    parser = ConfigParser()
    parser.read(   config_file )
    params = parser.items("POSTGRES")
    for param in params:
        db[param[0]] = param[1]
    return db


def get_connection_local_pg(params):
    """
    Return the Postgres db Connection

    :param db:
    :param config:
    :return:
    """
    #conn_string_no_passwd =  params

    #logging.info(conn_string_no_passwd)
    conn = psycopg2.connect(**params)

    cur = conn.cursor()
    logging.info('PostgreSQL database version:')
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    logging.info(db_version)
    # print(cursor)
    # conn.cursor will return a cursor object, you can use this cursor to perform queries

    return conn


def import_data(conn, path):
    cur = conn.cursor()
    create_sql = 'CREATE TABLE IF NOT EXISTS "i2b2_data"."public".pat_notes ( id SERIAL NOT NULL, file_name VARCHAR, note VARCHAR, PRIMARY KEY (id) )'
    res = cur.execute(create_sql)
    conn.commit()

    # Truncate table
    truncate_sql = 'TRUNCATE TABLE "i2b2_data"."public".pat_notes '
    res = cur.execute(truncate_sql)
    # Read files and import
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                logging.info(f"Importing file {entry.name}")
                with open(entry, 'r') as f:
                    data = f.read()
                    insert_sql = 'insert into "i2b2_data"."public".pat_notes(file_name, note) values (%s, %s) RETURNING id'
                    cur.execute(insert_sql, (entry.name,data,))
                    row_id = cur.fetchone()[0]
                    logging.info(f"Inserted row {row_id} ")
                    conn.commit()

    cur.close()
    conn.commit()
    return None