import psycopg2
from datetime import datetime, timedelta
import json
import os
import sys

# Check if the script is provided with a database name argument
if len(sys.argv) != 2:
    print("Usage: python script requires database name")
    sys.exit(1)

# Get the database name from the command-line argument
db_name = sys.argv[1]

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to config.json in the same directory as the script
config_path = os.path.join(script_dir, 'config.json')

# Read database configuration from config.json
with open(config_path, 'r') as config_file:
    db_config = json.load(config_file)

db_config['dbname'] = db_name

# SQL statement for creating the table
create_table_query = """
    CREATE TABLE IF NOT EXISTS TempReadings (
        id SERIAL PRIMARY KEY,
        sensor VARCHAR(255),
        name VARCHAR(255),
        temp DOUBLE PRECISION,
        date TIMESTAMP,
        guid VARCHAR(255),
        remarks TEXT
    )
"""

# Sample data to insert
sample_data = [
    (1, 'Sensor1', 'Location1', 25.5, datetime.now() -
     timedelta(days=1), 'guid1', 'Remarks 1'),
    (2, 'Sensor2', 'Location2', 24.0, datetime.now() -
     timedelta(days=1), 'guid2', 'Remarks 2'),
    (3, 'Sensor2', 'Location2', 27.0, datetime.now() -
     timedelta(days=1), 'guid2', 'Remarks 5'),
    (6, 'Sensor33', 'Location21', 21.0, datetime.now() -
     timedelta(days=1), 'guid2', 'Remarks 5'),
    (4, 'Sensor2', 'Location2', 26.0, datetime.now() +
     timedelta(days=1), 'guid3', 'Remarks 3'),
    (5, 'Sensor2', 'Location2', 23.0, datetime.now() -
     timedelta(days=2), 'guid3', 'Remarks 4'),
]

# SQL statement for inserting data
insert_query = """
    INSERT INTO TempReadings (id, sensor, name, temp, date, guid, remarks)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

try:
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute(create_table_query)

    for data in sample_data:
        cursor.execute(insert_query, data)

    conn.commit()
    print("Table created and data inserted successfully.")

except psycopg2.Error as e:
    conn.rollback()
    print("Error creating table or inserting data:", e)

finally:
    if conn:
        cursor.close()
        conn.close()
