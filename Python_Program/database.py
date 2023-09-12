import json
import psycopg2


def open_connection():
    # Read database configuration
    with open('config.json', 'r') as config_file:
        db_config = json.load(config_file)

    # Establish databse connection
    connection = psycopg2.connect(
        dbname=db_config['dbname'],
        user=db_config['user'],
        password=db_config['password'],
        host=db_config['host'],
        port=db_config['port']
    )

    return connection


def close_connection(con):
    # Close connection
    if con is not None:
        con.close()
